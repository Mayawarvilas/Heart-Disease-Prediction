function get_age(){
    var get_age=document.getElementById('age').value;
    return get_age;
}

function get_sex(){
    var get_sex=document.getElementById('sex').value;
    return get_sex;
}

function get_chestpain(){
    var get_chestpain=document.getElementById('chestpain').value;
    return get_chestpain;
}

function get_RestingBP(){
    var RestingBP=document.getElementById('RestingBP').value;
    return RestingBP;
}

function get_cholesterol(){
    var cholesterol=document.getElementById('Cholesterol').value;
    return cholesterol;
}

function get_FastingBS(){
    return document.getElementById('FastingBS').value;
}

function get_RestingECG(){
    return document.getElementById('RestingECG').value;
}

function get_MaxHR(){
    return document.getElementById('MaxHR').value;
}

function get_ExerciseAngina(){
    return document.getElementById('ExerciseAngina').value;
}

function get_OldPeak(){
    return document.getElementById('OldPeak').value;
}

function get_ST_Slope(){
    return document.getElementById('ST_Slope').value;
}


function onclickPredict(){
    var age=get_age()
    var sex=get_sex()
    var chestpain=get_chestpain()
    var restingBP=get_RestingBP()
    var cholesterol=get_cholesterol()
    var fastingBS=get_FastingBS()
    var restingECG=get_RestingECG()
    var maxHR=get_MaxHR()
    var exerciseAngina=get_ExerciseAngina()
    var oldPeak=get_OldPeak()
    var st_slope=get_ST_Slope()

    var result=document.getElementById('uirpedict');
    

    var url='http://127.0.0.1:5000/predict_heart_disease'

    $.post(url,{
        age:age,
        sex:sex,
        chestpain:chestpain,
        resting_bp:restingBP,
        cholesterol:cholesterol,
        fasting_bs:fastingBS,
        resting_ecg:restingECG,
        maxhr:maxHR,
        exercise_angina:exerciseAngina,
        oldpeak:oldPeak,
        slope:st_slope

    },function(data,status){
        console.log(data.Prediction);
        result.innerHTML='<h2>'+data.Prediction+'</h2>';

        if(data.Prediction ==='The Person Is Having Heart Disease'){
           result.style.color='red';
            
        }
        else{
            result.style.color='green';
            
        }
        
        console.log(status);
    })
}