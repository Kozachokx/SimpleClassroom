const list = [];
let obj = {
    nam : 'nameZ',
    sur : 'sukeZ'
}
list.push(obj)



function genereteAnswerFields(type,k = 4){
    let HTMLcode = ''
    let inputTypeField;
    if (type == 1) { inputTypeField='radio' }
    if (type == 2) { inputTypeField='checkbox' }
    if (type == 3) { inputTypeField='text' }
}
function genereteQuestionField(id){
    return `<label name="question_${id}">Question : </label> <input type="text">`
}


function generateQuizFields(){
    // let t1 = document.getElementById('type1').value
    // let t2 = document.getElementById('type2').value
    // let t3 = document.getElementById('type3').value

    var arr1 = [document.getElementById('type1').value, document.getElementById('type2').value, document.getElementById('type3').value ]

    let qbox = document.getElementById('qbox').innerHTML
    // console.log(`Type 1 = ${t1} \nType 2 = ${t2} \nType 3 = ${t3} \nq : ${qbox}\n${arr1}`)
    console.log(`q : ${qbox}\n${arr1}`)

    let HTMLbox = ''

    for(let qType=1; qType<=3; qType++){
        HTMLbox += `<div id="qType_${qType}"><h2>Type ${qType} (${arr1[qType-1]})</h2><ol><li>`

            for(let qId=1; qId<=arr[qType-1]; qId++){
                HTMLbox += 
            }
            
        HTMLbox += `</li></ol><hr><div>`
    }

    qbox = HTMLbox

}


function getFields(){
    for(let i=1; i<=3; i++){
        let HTMLdiv = document.getElementById(`qType_${i}`)

        for(let j=1; j<=arr[i-1]; j++){
         console.log(`${i}_type question_${j}`)   
        }
    }
}
/*
`
-FOR_LOOP-
<div id="qType_${qId}">

    <h2>Type ${qId} (${t1}})</h2>
        <ol>
            <li>
            --FOR_LOOP--
                <label name="question_${qId}">Question : </label>
                <input type="text" id="questionField_${qId}">
                <p>Answers:</p>
                <ul>
                ---FOR_LOOP---
                    <li><input type="radio" name="question_1"> <input type="text"></li>
                ---
                </ul>
            ---
            </li>
        </ol>

</div>
-
`

*/