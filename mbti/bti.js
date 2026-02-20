const jbti = document.querySelector("#kkk");
const button = document.querySelector("#strbutton");

const retryu = document.querySelector("#retry");

const kingone = document.querySelector("#kingone");
const kingtwo = document.querySelector("#kingtwo");
const kingthree = document.querySelector("#kingthree");
const kingfour = document.querySelector("#kingfour");
const kingfive = document.querySelector("#kingfive");
const kingsix = document.querySelector("#kingsix");
const kingseven = document.querySelector("#kingseven");
const kingeight = document.querySelector("#kingeight");
const kingnine = document.querySelector("#kingnine");
const kingten = document.querySelector("#kingten");
const kingeleven = document.querySelector("#kingeleven");
const kingtwelve = document.querySelector("#kingtwelve");

const entj = document.querySelector("#entj");
const intj = document.querySelector("#intj");
const estj = document.querySelector("#estj");
const istj = document.querySelector("#istj");
const enfj = document.querySelector("#enfj");
const infj = document.querySelector("#infj");
const esfj = document.querySelector("#esfj");
const isfj = document.querySelector("#isfj");
const entp = document.querySelector("#entp");
const intp = document.querySelector("#intp");
const estp = document.querySelector("#estp");
const istp = document.querySelector("#istp");
const enfp = document.querySelector("#enfp");
const infp = document.querySelector("#infp");
const esfp = document.querySelector("#esfp");
const isfp = document.querySelector("#isfp");

istj.style.display = 'none';
isfj.style.display = 'none';
infj.style.display = 'none';
intj.style.display = 'none';
istp.style.display = 'none';
isfp.style.display = 'none';
infp.style.display = 'none';
intp.style.display = 'none';
estp.style.display = 'none';
esfp.style.display = 'none';
enfp.style.display = 'none';
entp.style.display = 'none';
estj.style.display = 'none';
esfj.style.display = 'none';
enfj.style.display = 'none';
entj.style.display = 'none';

const akf1 = document.querySelector("#akf1");
const akf2 = document.querySelector("#akf2");

const duru = document.querySelector("#duru")
const duru1 = document.querySelector("#duru1")

retryu.style.display = 'none';


duru.style.display = 'none';
duru1.style.display = 'none';

akf1.style.display = 'none';
akf2.style.display = 'none';

kingone.style.display = "none";
kingtwo.style.display = 'none';
kingthree.style.display = 'none';
kingfour.style.display = 'none';
kingfive.style.display = 'none';
kingsix.style.display = 'none';
kingseven.style.display = 'none';
kingeight.style.display = 'none';
kingnine.style.display = 'none';
kingten.style.display = 'none';
kingeleven.style.display = 'none';
kingtwelve.style.display = 'none';



var ar = ['사형', '사혀영영']

var array = [];
var a = 0;

function asdf(app){
    array.push(app);
    console.log('dfkdj');
    
    if (array.length == 1){
        kingone.style.display = "none";
        duru.style.display = "none";
        akf1.style.display = 'none';
        kingtwo.style.display = "block";
        duru1.style.display = "block";
        akf2.style.display = 'block';

    }
    if (array.length == 2){
        kingtwo.style.display = "none";
        duru1.style.display = "none";
        akf2.style.display = 'none';
        kingthree.style.display = "block";
        duru.style.display = "block";
        akf1.style.display = 'block';
        console.log(array[0])
    }
    if (array.length == 3){
        kingthree.style.display = "none";
        duru.style.display = "none";
        akf1.style.display = 'none';
        kingfour.style.display = "block";
        duru1.style.display = "block";
        akf2.style.display = 'block';
        console.log(array)
    }
    if (array.length == 4){
        kingfour.style.display = "none";
        duru1.style.display = "none";
        akf2.style.display = 'none';
        kingfive.style.display = "block";
        duru.style.display = "block";
        akf1.style.display = 'block';
        console.log(array)
    }
    if (array.length == 5){
        kingfive.style.display = "none";
        duru.style.display = "none";
        akf1.style.display = 'none';
        kingsix.style.display = "block";
        duru1.style.display = "block";
        akf2.style.display = 'block';
        console.log(array)
    }
    if (array.length == 6){
        kingsix.style.display = "none";
        duru1.style.display = "none";
        akf2.style.display = 'none';
        kingseven.style.display = "block";
        duru.style.display = "block";
        akf1.style.display = 'block';
        console.log(array)
    }
    if (array.length == 7){
        kingseven.style.display = "none";
        duru.style.display = "none";
        akf1.style.display = 'none';
        kingeight.style.display = "block";
        duru1.style.display = "block";
        akf2.style.display = 'block';
        console.log(array)
    }
    if (array.length == 8){
        kingeight.style.display = "none";
        duru1.style.display = "none";
        akf2.style.display = 'none';
        kingnine.style.display = "block";
        duru.style.display = "block";
        akf1.style.display = 'block';
        console.log(array)
    }
    if (array.length == 9){
        kingnine.style.display = "none";
        duru.style.display = "none";
        akf1.style.display = 'none';
        kingten.style.display = "block";
        duru1.style.display = "block";
        akf2.style.display = 'block';
        console.log(array)
    }
    if (array.length == 10){
        kingten.style.display = "none";
        duru1.style.display = "none";
        akf2.style.display = 'none';
        kingeleven.style.display = "block";
        duru.style.display = "block";
        akf1.style.display = 'block';
        console.log(array)
    }
    if (array.length == 11){
        kingeleven.style.display = "none";
        duru.style.display = "none";
        akf1.style.display = 'none';
        kingtwelve.style.display = "block";
        duru1.style.display = "block";
        akf2.style.display = 'block';
        console.log(array)
    }
    if (array.length == 12){
        kingtwelve.style.display = "none";
        duru1.style.display = "none";
        akf2.style.display = 'none';
        console.log(array)
        retryu.style.display = 'block';
        last()
    }

}

function last(){
    e = array[0] + array[8] + array[10];
    n = array[9] + array[1] + array[6];
    t = array[7] + array[3] + array[11];
    j = array[5] + array[2] + array[4];
    if (e >= 2){
        if (n >= 2){
            if (t>=2){
                if(j>=2){
                    entj.style.display='block';
                }
                else{
                    entp.style.display = 'block';
                }
            }
            else{
                if (j>=2){
                    enfj.style.display = 'block';
                }
                else{
                    enfp.style.display = 'block';
                }
            }
        }
        else{
            if (t>=2){
                if(j>=2){
                    estj.style.display='block';
                }
                else{
                    estp.style.display = 'block';
                }
            }
            else{
                if (j>=2){
                    esfj.style.display = 'block';
                }
                else{
                    esfp.style.display = 'block';
                }
            }
        }
    }
    else{
        if (n >= 2){
            if (t>=2){
                if(j>=2){
                    intj.style.display='block';
                }
                else{
                    intp.style.display = 'block';
                }
            }
            else{
                if (j>=2){
                    infj.style.display = 'block';
                }
                else{
                    infp.style.display = 'block';
                }
            }
        }
        else{
            if (t>=2){
                if(j>=2){
                    istj.style.display='block';
                }
                else{
                    istp.style.display = 'block';
                }
            }
            else{
                if (j>=2){
                    isfj.style.display = 'block';
                }
                else{
                    isfp.style.display = 'block';
                }
            }
        }
    }
}
function retry(){
    array = [];
    retryu.style.display = 'none';
    istj.style.display = 'none';
    isfj.style.display = 'none';
    infj.style.display = 'none';
    intj.style.display = 'none';
    istp.style.display = 'none';
    isfp.style.display = 'none';
    infp.style.display = 'none';
    intp.style.display = 'none';
    estp.style.display = 'none';
    esfp.style.display = 'none';
    enfp.style.display = 'none';
    entp.style.display = 'none';
    estj.style.display = 'none';
    esfj.style.display = 'none';
    enfj.style.display = 'none';
    entj.style.display = 'none';

    duru.style.display = 'none';
    duru1.style.display = 'none';

    akf1.style.display = 'none';
    akf2.style.display = 'none';

    kingone.style.display = "none";
    kingtwo.style.display = 'none';
    kingthree.style.display = 'none';
    kingfour.style.display = 'none';
    kingfive.style.display = 'none';
    kingsix.style.display = 'none';
    kingseven.style.display = 'none';
    kingeight.style.display = 'none';
    kingnine.style.display = 'none';
    kingten.style.display = 'none';
    kingeleven.style.display = 'none';
    kingtwelve.style.display = 'none';

    jbti.style.display = 'block';
    button.style.display = 'block';

}
function asd(){
    jbti.style.display = "none";
    button.style.display = "none";
    
    duru.style.display = "block";
    kingone.style.display = "block";
    akf1.style.display = 'block';
}

button.addEventListener("click",asd);







