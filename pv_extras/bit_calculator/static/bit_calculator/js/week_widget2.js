const container = document.getElementById("weekly_bit_rewards_container");
const addButton = document.getElementById("add_week_btn");
const totalForms = document.getElementById("id_form-TOTAL_FORMS");

addButton.addEventListener("click", () => {
    const formCount = parseInt(totalForms.value);
    
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
    newWeekElemDiv.classList.add('flex', 'flex-row', 'pb-2', 'gap-x-2', 'form-row');
    
    newWeekElemP.classList.add('self-center', 'px-1', 'test-sm', 'text-base-content');
    newWeekElemP.innerText = 'Week ' + formCount;
    
    newWeekElemInput.classList.add('required', 'input', 'input-primary', 'validator', 'w-80');
    newWeekElemInput.type = 'number';
    newWeekElemInput.name = 'bitRewards';
    newWeekElemInput.value = 5;
    newWeekElemInput.min = 0;
    newWeekElemInput.id = 'id_bitRewards';

    newWeekElemValidatorP.classList.add('hidden', 'validator-hint');
    newWeekElemValidatorP.textContent = "Invalid Amount";

    newWeekElemDeleteBtn.classList.add('btn', 'btn-error', 'w-20', 'text-sm', 'remove-form');
    newWeekElemDeleteBtn.type = 'button';
    newWeekElemDeleteBtn.innerText = 'Remove';

    newWeekElem.innerHTML = newWeekElem.innerHTML.replace(
        /form-(\d)+/g,
        `form-${formCount}`
    );

    container.appendChild(newWeekElem);
    totalForms.value = parseInt(totalForms.value) + 1;

    if (totalForms.value == 20){
        addButton.disabled = true;
    }
    else{
        addButton.disabled = false;
    }
});

container.addEventListener("click", e => {
    if (e.target.classList.contains("remove-form")) {
        const formRow = e.target.closest(".form-row");

        // If DELETE exists, mark instead of removing
        const deleteInput = formRow.querySelector('input[type="checkbox"][name$="DELETE"]');
        if (deleteInput) {
            deleteInput.checked = true;
            formRow.style.display = "none";
        } else {
            formRow.remove();
            totalForms.value = parseInt(totalForms.value) - 1;
        }
    }
});
