const THEMES = [
  { key:'red', name:'红', tones:{100:'#F7E7E5',300:'#EECFCC',500:'#E6BAB6',700:'#B7837E'} },
  { key:'orange', name:'橙', tones:{100:'#F5E8E0',300:'#EBD2C2',500:'#E2BEA7',700:'#B2886C'} },
  { key:'yellow', name:'黄', tones:{100:'#EFEBDE',300:'#DED8BE',500:'#D1C7A1',700:'#9E9264'} },
  { key:'green', name:'绿', tones:{100:'#E4EFE4',300:'#CADECA',500:'#B2D0B2',700:'#7A9D7A'} },
  { key:'cyan', name:'青', tones:{100:'#DEEFF0',300:'#BEDFE1',500:'#A0D1D4',700:'#609FA2'} },
  { key:'blue', name:'蓝', tones:{100:'#E3ECF7',300:'#C8D9EF',500:'#B0C9E8',700:'#7795BA'} },
  { key:'purple', name:'紫', tones:{100:'#EEE8F5',300:'#DDD2EB',500:'#CEBFE2',700:'#9B88B3'} },
  { key:'gray', name:'灰', tones:{100:'#E9EBEE',300:'#D5D8DB',500:'#C3C7CC',700:'#8D939A'} }
];
function setTheme(key){
  const theme=THEMES.find(item=>item.key===key)||THEMES[5];
  [100,300,500,700].forEach(step=>document.documentElement.style.setProperty(`--p${step}`,theme.tones[step]));
  document.querySelectorAll('[data-tone]').forEach(item=>{item.textContent=theme.tones[item.dataset.tone]});
  document.querySelectorAll('.hue-btn').forEach(button=>{const active=button.dataset.theme===theme.key;button.classList.toggle('is-active',active);button.setAttribute('aria-pressed',String(active))});
  document.getElementById('themeName').textContent=`${theme.name}${theme.key==='purple'?' / 默认':''}`;
  try{localStorage.setItem('designSpecThemeV06',theme.key)}catch(error){console.info('主题存储不可用',error)}
}
function buildGrid(){
  const stage=document.getElementById('gridStage');if(!stage)return;
  const fragment=document.createDocumentFragment();
  for(let row=0;row<Math.ceil(stage.clientHeight/4);row+=1){for(let column=0;column<Math.ceil(stage.clientWidth/4);column+=1){const cell=document.createElement('i');cell.className='micro-cell';cell.style.left=`${column*4}px`;cell.style.top=`${row*4}px`;fragment.appendChild(cell)}}
  stage.prepend(fragment);
}
function initDiagramScale(){
  const frame=document.getElementById('diagramFrame');if(!frame)return;
  const update=()=>{const scale=Math.min(frame.clientWidth/1120,frame.clientHeight/630);frame.style.setProperty('--diagram-scale',String(scale))};
  update();if('ResizeObserver' in window){new ResizeObserver(update).observe(frame)}else{window.addEventListener('resize',update,{passive:true})}
}
function init(){
  buildGrid();initDiagramScale();
  const list=document.getElementById('hueList');
  THEMES.forEach(theme=>{const button=document.createElement('button');button.type='button';button.className='hue-btn';button.dataset.theme=theme.key;button.style.backgroundColor=theme.tones[500];button.innerHTML=`<span>${theme.name}</span><small>${theme.tones[500]}</small>`;button.addEventListener('click',()=>setTheme(theme.key));list.appendChild(button)});
  let saved='purple';try{saved=localStorage.getItem('designSpecThemeV06')||saved}catch(error){console.info('使用默认主题',error)}setTheme(saved);
}
init();
