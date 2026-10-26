const COMPANIES=['Square','Incepta','Beximco','Renata','ACI','Opsonin','Eskayef'];
const DRUGS=[
{name:'Propofol 1% 200mg/20ml',cls:'IV anaesthetic',dose:'Induction 2-2.5 mg/kg IV; Maint 100-200 mcg/kg/min',ind:'Induction/maintenance of GA; ICU sedation',ci:'Egg/soy allergy; hemodynamic instability; raised ICP',p:[180,165,170,190,175,160,185]},
{name:'Ketamine 50mg/ml 10ml',cls:'IV anaesthetic',dose:'1-2 mg/kg IV; 4-6 mg/kg IM',ind:'Induction; analgesia; procedural sedation',ci:'Raised ICP; psychosis; uncontrolled HTN; glaucoma',p:[120,110,115,130,125,105,128]},
{name:'Thiopental Na 500mg',cls:'IV anaesthetic',dose:'3-5 mg/kg IV',ind:'Induction of GA',ci:'Porphyria; asthma; CV instability; airway obstruction',p:[90,85,88,95,92,80,93]},
{name:'Etomidate 20mg/10ml',cls:'IV anaesthetic',dose:'0.2-0.3 mg/kg IV',ind:'Induction in hemodynamically unstable',ci:'Adrenal insufficiency; sepsis (relative)',p:[450,430,440,460,435,420,455]},
{name:'Midazolam 5mg/5ml',cls:'Benzodiazepine',dose:'0.02-0.1 mg/kg IV; 0.5-0.7 mg/kg PO (ped)',ind:'Anxiolysis; sedation; premedication',ci:'Acute narrow-angle glaucoma; shock; myasthenia',p:[60,55,58,65,62,52,63]},
{name:'Fentanyl 50mcg/ml 10ml',cls:'Opioid',dose:'1-2 mcg/kg IV; 0.5-1 mcg/kg/hr infusion',ind:'Analgesia; adjunct to GA',ci:'MAO inhibitors; respiratory depression; raised ICP',p:[150,140,145,160,155,135,158]},
{name:'Morphine 10mg/ml 1ml',cls:'Opioid',dose:'0.1-0.2 mg/kg IV/IM',ind:'Analgesia; premedication',ci:'Respiratory depression; raised ICP; hypotension',p:[45,42,44,48,46,40,47]},
{name:'Sufentanil 50mcg/ml 2ml',cls:'Opioid',dose:'0.1-0.5 mcg/kg IV',ind:'Analgesia; cardiac anaesthesia',ci:'Respiratory depression; opioid allergy',p:[320,305,310,335,318,295,330]},
{name:'Remifentanil 2mg vial',cls:'Opioid',dose:'0.5-1 mcg/kg bolus; 0.05-0.5 mcg/kg/min',ind:'Intraop analgesia; TIVA',ci:'Respiratory depression; opioid allergy',p:[900,870,880,920,890,850,910]},
{name:'Rocuronium 50mg/5ml',cls:'NM blocker',dose:'0.6-1.2 mg/kg IV (RSI 1.2)',ind:'NMB for intubation/surgery',ci:'Hypersensitivity; malignant hyperthermia risk',p:[260,245,250,275,265,240,270]},
{name:'Vecuronium 4mg vial',cls:'NM blocker',dose:'0.08-0.12 mg/kg IV',ind:'NMB during surgery',ci:'Hypersensitivity; severe renal/hepatic disease',p:[180,170,175,190,185,165,188]},
{name:'Atracurium 25mg/ml 5ml',cls:'NM blocker',dose:'0.4-0.5 mg/kg IV',ind:'NMB during surgery',ci:'Hypersensitivity; asthma (histamine release)',p:[210,198,205,225,215,190,220]},
{name:'Cisatracurium 10mg/5ml',cls:'NM blocker',dose:'0.1-0.2 mg/kg IV',ind:'NMB; ICU; organ dysfunction',ci:'Hypersensitivity',p:[300,285,290,315,305,275,310]},
{name:'Suxamethonium 50mg/ml 2ml',cls:'Depolarizing NM blocker',dose:'1-2 mg/kg IV (ped 2 mg/kg)',ind:'RSI; short procedures',ci:'Hyperkalemia; burns; MH; pseudocholinesterase deficiency',p:[55,50,52,58,56,48,57]},
{name:'Neostigmine 0.5mg/ml 1ml',cls:'Reversal',dose:'0.04-0.07 mg/kg IV (+glycopyrrolate)',ind:'Reversal of NMB',ci:'Mechanical obstruction; peritonitis; urinary obstruction',p:[35,32,33,38,36,30,37]},
{name:'Sugammadex 100mg/ml 2ml',cls:'Reversal',dose:'2-4 mg/kg IV (16 for RSI)',ind:'Reversal of rocuronium/vecuronium',ci:'Severe renal impairment; hypersensitivity',p:[1800,1750,1760,1850,1800,1700,1820]},
{name:'Sevoflurane 250ml',cls:'Inhalational anaesthetic',dose:'Induction 8%; Maint 1-3% (MAC 2.0)',ind:'Induction/maintenance; pediatrics',ci:'MH susceptibility; severe hypovolemia',p:[4200,4000,4100,4400,4250,3900,4350]},
{name:'Isoflurane 100ml',cls:'Inhalational anaesthetic',dose:'Maint 1-2% (MAC 1.15)',ind:'Maintenance of GA',ci:'MH susceptibility; ICP (relative)',p:[1800,1700,1750,1900,1820,1650,1880]},
{name:'Desflurane 240ml',cls:'Inhalational anaesthetic',dose:'Maint 4-6% (MAC 6.0)',ind:'Maintenance; fast emergence',ci:'MH susceptibility; airway irritant',p:[6500,6200,6300,6700,6550,6100,6650]},
{name:'Halothane 250ml',cls:'Inhalational anaesthetic',dose:'Induction 2-4%; Maint 0.5-1.5%',ind:'Pediatric induction (historical)',ci:'Hepatotoxicity; MH; ICP',p:[1500,1400,1450,1550,1500,1350,1530]},
{name:'Nitrous Oxide (cylinder)',cls:'Inhalational anaesthetic',dose:'50-70% with O2',ind:'Analgesia; adjunct',ci:'Pneumothorax; bowel obstruction; B12 deficiency',p:[0,0,0,0,0,0,0]},
{name:'Lidocaine 2% 50ml',cls:'Local anaesthetic',dose:'Max 4.5 mg/kg (7 with adren)',ind:'Local/regional; IV (ventricular arrhythmia)',ci:'Heart block; hypersensitivity; porphyria (relative)',p:[80,75,78,85,82,70,84]},
{name:'Bupivacaine 0.5% 20ml',cls:'Local anaesthetic',dose:'Max 2 mg/kg (3 with adren)',ind:'Spinal/epidural; nerve blocks',ci:'Hypersensitivity; severe hypotension; heart block',p:[95,88,90,100,96,82,98]},
{name:'Ropivacaine 0.75% 20ml',cls:'Local anaesthetic',dose:'Max 3 mg/kg',ind:'Epidural; nerve blocks; postop analgesia',ci:'Hypersensitivity; hypovolemia',p:[140,130,135,148,142,125,146]},
{name:'Ondansetron 4mg/2ml',cls:'Antiemetic',dose:'0.1-0.15 mg/kg IV (max 4mg)',ind:'PONV prophylaxis/treatment',ci:'QT prolongation; hypersensitivity',p:[25,22,23,28,26,20,27]},
{name:'Dexamethasone 4mg/ml 1ml',cls:'Corticosteroid',dose:'0.1-0.2 mg/kg IV (max 8mg)',ind:'PONV; airway edema; cerebral edema',ci:'Active infection; uncontrolled diabetes',p:[12,10,11,13,12,9,12]},
{name:'Paracetamol 1000mg/100ml IV',cls:'Analgesic/antipyretic',dose:'15 mg/kg IV (max 1g, 4g/day)',ind:'Mild-moderate pain; fever',ci:'Severe hepatic impairment; overdose risk',p:[110,100,105,120,115,95,118]},
{name:'Dexmedetomidine 100mcg/ml 2ml',cls:'Alpha-2 agonist',dose:'0.5-1 mcg/kg load; 0.2-0.7 mcg/kg/hr',ind:'Sedation; adjunct analgesia',ci:'Heart block; severe ventricular dysfunction',p:[350,330,335,365,355,320,360]},
{name:'Atropine 1mg/ml 1ml',cls:'Anticholinergic',dose:'0.01-0.02 mg/kg IV (min 0.1mg)',ind:'Bradycardia; antisialagogue',ci:'Glaucoma; obstructive uropathy; tachycardia',p:[15,13,14,16,15,12,16]},
{name:'Glycopyrrolate 0.2mg/ml 1ml',cls:'Anticholinergic',dose:'0.004-0.01 mg/kg IV',ind:'Bradycardia; reduce secretions',ci:'Glaucoma; obstructive uropathy',p:[28,25,26,30,29,23,29]},
{name:'Ephedrine 30mg/ml 1ml',cls:'Vasopressor',dose:'5-10 mg IV bolus',ind:'Hypotension (spinal/anaesthesia)',ci:'Severe HTN; tachyarrhythmia; pheochromocytoma',p:[40,37,38,42,40,35,41]},
{name:'Phenylephrine 10mg/ml 1ml',cls:'Vasopressor',dose:'50-100 mcg IV bolus; 0.1-0.5 mcg/kg/min',ind:'Hypotension; maintain perfusion',ci:'Severe bradycardia; peripheral vascular disease',p:[55,50,52,58,56,48,57]},
{name:'Naloxone 0.4mg/ml 1ml',cls:'Opioid antagonist',dose:'0.04-0.4 mg IV (titrate)',ind:'Opioid reversal; respiratory depression',ci:'Opioid-dependent (precipitates withdrawal)',p:[30,27,28,32,31,26,31]},
{name:'Flumazenil 0.1mg/ml 5ml',cls:'Benzodiazepine antagonist',dose:'0.1-0.2 mg IV (max 1mg)',ind:'Benzodiazepine reversal',ci:'Seizure-prone; TCA overdose; raised ICP',p:[220,205,210,235,225,195,230]},
{name:'Dantrolene 20mg vial',cls:'MH antidote',dose:'2.5 mg/kg IV (max 10 mg/kg)',ind:'Malignant hyperthermia',ci:'None absolute (emergency use)',p:[950,900,920,980,960,880,970]}
];
function renderDrugRef(){
  const q=(document.getElementById('drugQ')?.value||'').toLowerCase();
  const ci=parseInt(document.getElementById('drugCo')?.value||'0');
  const tbody=document.querySelector('#drugTable tbody');
  if(!tbody) return;
  const rows=DRUGS.filter(d=>!q||d.name.toLowerCase().includes(q)||d.cls.toLowerCase().includes(q)||d.ind.toLowerCase().includes(q)||d.ci.toLowerCase().includes(q));
  tbody.innerHTML=rows.map(d=>{
    const price=d.p[ci]||0;
    const usd=price? (price/110).toFixed(2):'-';
    const inr=price? (price/1.32).toFixed(2):'-';
    const kwd=price? (price/358).toFixed(3):'-';
    return '<tr style="border-bottom:1px solid #f1f5f9">'+
      '<td style="padding:4px"><b>'+d.name+'</b></td>'+
      '<td>'+d.cls+'</td><td>'+d.dose+'</td><td>'+d.ind+'</td><td>'+d.ci+'</td>'+
      d.p.map(x=>'<td style="text-align:right">'+(x?x:'-')+'</td>').join('')+
      '<td style="text-align:right">'+usd+'</td><td style="text-align:right">'+inr+'</td><td style="text-align:right">'+kwd+'</td>'+
      '</tr>';
  }).join('');
}
