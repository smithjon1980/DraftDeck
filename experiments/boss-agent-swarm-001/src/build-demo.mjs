import{buildPdf}from'./pdf-worker.mjs';
const [source='fixtures/day-zero.html',output='output/day-zero.pdf']=process.argv.slice(2);
console.log(JSON.stringify(await buildPdf({source,output}),null,2));
