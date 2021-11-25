//console.log('hello world')

/*
JavaScript used to generate modal dialog buttons from quiz database using Django MVC architecture
*/
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

// for each button in main page display a modal dialog when clicked
modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    // console.log(time)
    // console.log(difficulty)

    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>difficulty: <b>${difficulty}</b></li>
                <li>number of questions: <b>${numQuestions}</b></li>
                <li>score to pass: <b>${scoreToPass}%</b></li>
                <li>time: <b>${time} min</b></li>

            </ul>
        </div>
    `
    // listen for click event on start button which will change the web page to the primary key and data url
    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk +"/data/"
    })
}))