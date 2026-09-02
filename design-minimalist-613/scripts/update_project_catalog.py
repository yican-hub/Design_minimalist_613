#!/usr/bin/env python3
"""将已确认的设计项目沉淀到 design-minimalist-613 的项目目录与注册表。"""

import argparse
import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
PROJECTS_MD = REFERENCES / "PROJECTS.md"
REGISTRY = REFERENCES / "project-registry.json"
PROJECT_ASSETS = ROOT / "assets" / "template" / "projects"


def parse_args():
    parser = argparse.ArgumentParser(description="新增或更新设计项目 preset")
    parser.add_argument("--slug", required=True, help="小写连字符项目 ID")
    parser.add_argument("--title", required=True, help="项目类型名称")
    parser.add_argument("--canvas", required=True, help="固定画板，如 1440x810 / 16:9")
    parser.add_argument("--priority", required=True, choices=["image-first", "text-first", "balanced"])
    parser.add_argument("--summary", required=True, help="已泛化的项目方法摘要，不写业务敏感内容")
    parser.add_argument("--preset-file", type=Path, help="可选 preset.yaml")
    parser.add_argument("--example-html", type=Path, help="可选已确认的 HTML 源实例")
    parser.add_argument("--asset-dir", type=Path, help="可选项目资产目录")
    return parser.parse_args()


def validate_slug(slug):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise SystemExit("slug 必须使用小写字母、数字与连字符")


def copy_optional(source, target):
    if not source:
        return
    source = source.resolve()
    if not source.exists():
        raise SystemExit(f"输入不存在：{source}")
    if source.is_dir():
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def update_registry(args):
    data = json.loads(REGISTRY.read_text(encoding="utf-8")) if REGISTRY.exists() else {"version": 1, "projects": []}
    item = {
        "slug": args.slug,
        "title": args.title,
        "canvas": args.canvas,
        "priority": args.priority,
        "status": "confirmed",
        "updated_at": date.today().isoformat(),
    }
    projects = [project for project in data.get("projects", []) if project.get("slug") != args.slug]
    projects.append(item)
    data["projects"] = sorted(projects, key=lambda project: project["slug"])
    REGISTRY.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_projects_md(args):
    start = f"<!-- AUTO_PROJECT:{args.slug} START -->"
    end = f"<!-- AUTO_PROJECT:{args.slug} END -->"
    source_line = f"source: assets/template/projects/{args.slug}/example.html\n" if args.example_html else ""
    block = f"""{start}
## project:{args.slug}

```yaml
project: {args.slug}
canvas: \"{args.canvas}\"
priority: {args.priority}
{source_line}preset: assets/template/projects/{args.slug}/preset.yaml
```

{args.summary.strip()}
{end}"""
    text = PROJECTS_MD.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(start) + r"[\s\S]*?" + re.escape(end))
    if pattern.search(text):
        text = pattern.sub(block, text)
    else:
        marker = "\n## Loop 累积项目\n"
        if marker not in text:
            text = text.rstrip() + marker
        text = text.rstrip() + "\n\n" + block + "\n"
    PROJECTS_MD.write_text(text, encoding="utf-8")


def write_default_preset(args, target):
    preset = target / "preset.yaml"
    if args.preset_file:
        copy_optional(args.preset_file, preset)
        return
    preset.write_text(
        f'project: {args.slug}\ncanvas: "{args.canvas}"\npriority: {args.priority}\nresponsive_reflow: false\n',
        encoding="utf-8",
    )


def main():
    args = parse_args()
    validate_slug(args.slug)
    target = PROJECT_ASSETS / args.slug
    target.mkdir(parents=True, exist_ok=True)
    write_default_preset(args, target)
    copy_optional(args.example_html, target / "example.html")
    copy_optional(args.asset_dir, target / "assets")
    update_registry(args)
    update_projects_md(args)
    print(json.dumps({"status": "ok", "project": args.slug, "project_dir": str(target)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
