function addItem() {
    document.querySelector('#add-item').insertAdjacentHTML(
        'afterend',
        `<div class="todo-item">
            <input type="checkbox" name="new">
            <label class="todo-item-label">new &emsp;</label>
            <button class="del-task-btn">Delete</button>
        </div>`
    )
}