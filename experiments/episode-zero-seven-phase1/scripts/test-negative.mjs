import assert from 'node:assert/strict';import {validate} from './validate.mjs';import {plans} from './layouts.mjs';
let n=0;const clone=()=>structuredClone(plans);function test(name,args,ok){const r=validate(args);assert.equal(r.pass,ok,name+':'+r.errors);n++;console.log('PASS',name)}
test('photorealism accepted',{},true);test('illustration accepted',{medium:'EDITORIAL_ILLUSTRATION'},true);test('red rejected',{colors:['#FF0000']},false);test('green rejected',{colors:['#00FF00']},false);test('dark page rejected',{background:'#000000'},false);test('full-bleed dark rejected',{darkFullBleed:true},false);test('dark HUD medium rejected',{medium:'DARK_MODE_PAGE'},false);test('1920x1080 rejected',{page:[1920,1080]},false);
let a=clone();delete a[0].zones.notes;test('missing zone rejected',{layouts:a},false);
a=clone();a[0].zones.notes=[...a[0].zones.illustration];test('overlap rejected',{layouts:a},false);
a=clone();a[2].zones.notes[0]=17;test('out of bounds rejected',{layouts:a},false);
a=clone();a[1]=structuredClone(a[0]);test('duplicate layout rejected',{layouts:a},false);
test('six layouts rejected',{layouts:clone().slice(0,6)},false);
console.log('PASS '+n+' targeted tests; NO visual, source, or browser qualification claimed');
