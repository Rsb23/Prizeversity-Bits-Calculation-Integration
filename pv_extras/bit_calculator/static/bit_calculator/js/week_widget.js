const addWeekBtn = document.getElementById("add_week_btn");
const weekContainer = document.getElementById("weekly_bit_rewards_container");
const weekCountElem = document.getElementById("weekCount");


function addWeek(){
    let weekCount = weekCountElem.innerText;
    weekCount++;
    weekCountElem.innerText = weekCount;

    // can't just paste desired HTML to innerHTML because it won't get formatted by daisyUI
    // need to create each element, nest them, and add individual classes
    const newWeekElem = document.createElement('li');
    const newWeekElemDiv = document.createElement('div');
    const newWeekElemP = document.createElement('p');
    const newWeekElemFieldset = document.createElement('fieldset');
    const newWeekElemInput = document.createElement('input');
    const newWeekElemValidatorP = document.createElement('p');
    const newWeekElemDeleteBtn = document.createElement('button')
    /*
    <li>
        <div class="flex flex-row pb-2 gap-x-2">
            <p class="self-center px-1 text-sm text-base-content">Week 1</p>
            <fieldset>
                <input type="number" name="bitRewards" value="5" min="0" class="required input input-primary validator w-100" required="" id="id_bitRewards">
                <p class="hidden validator-hint">Invalid Bit Amount</p>
            </fieldset>
        </div>
        delete button
    </li> 
    */
    // nest created elements
    newWeekElem.appendChild(newWeekElemDiv);

    newWeekElemDiv.appendChild(newWeekElemP);
    newWeekElemDiv.appendChild(newWeekElemFieldset);
    newWeekElemDiv.appendChild(newWeekElemDeleteBtn);

    newWeekElemFieldset.appendChild(newWeekElemInput);
    newWeekElemFieldset.appendChild(newWeekElemValidatorP);

    // add formatting / daisyUI classes / other attributes
    newWeekElemDiv.classList.add('flex', 'flex-row', 'pb-2', 'gap-x-2');
    
    newWeekElemP.classList.add('self-center', 'px-1', 'test-sm', 'text-base-content');
    newWeekElemP.innerText = 'Week ' + weekCount;
    newWeekElemP
    
    newWeekElemInput.classList.add('required', 'input', 'input-primary', 'validator', 'w-80');
    newWeekElemInput.type = 'number';
    newWeekElemInput.name = 'bitRewards';
    newWeekElemInput.value = 5;
    newWeekElemInput.min = 0;
    newWeekElemInput.id = 'id_bitRewards';

    newWeekElemValidatorP.classList.add('hidden', 'validator-hint');

    newWeekElemDeleteBtn.classList.add('btn', 'btn-error', 'w-20');
    newWeekElemDeleteBtn.type = 'button';
    newWeekElemDeleteBtn.innerText = 'Remove';
    newWeekElemDeleteBtn.addEventListener('click', removeSelf);

    // add elements
    weekContainer.appendChild(newWeekElem);
    weekContainer.scrollTop = weekContainer.scrollHeight;

    if (weekCount == 20){
        addWeekBtn.disabled = true;
    }
    else{
        addWeekBtn.disabled = false;
    }
}

function removeSelf(){
    let weekCount = weekCountElem.innerText;

    weekCount--;
    weekCountElem.innerText = weekCount;

    this.parentElement.parentElement.remove();

    if (weekCount == 20){
        addWeekBtn.disabled = true;
    }
    else{
        addWeekBtn.disabled = false;
    }
}
