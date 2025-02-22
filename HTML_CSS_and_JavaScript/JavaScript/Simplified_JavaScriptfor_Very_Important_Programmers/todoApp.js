const taskInput = document.querySelector("#taskInput");
const taskList = document.querySelector("#taskList");
const addTaskForm = document.querySelector("#addTaskForm");

taskList.style = `
    list-style: none; 
    margin-top: 1rem; 
    font-size: 1.5rem`;

const createTaskItem = (task) => `
    <li>
        <input type="checkbox" name="task" value="${task}" onChange="toggleTaskCompletion(event)"/>
        <label for="task">${task}</label>
        <button type="button" onClick="removeTask(event)">X</button>
    </li> `

const storedTasks = JSON.parse(localStorage.getItem("tasks")) || [];

const renderTasks = () => {
    storedTasks.foreach((task) => {
        taskList.insertAdjacentHTML("beforeend", createTaskItem(task))
    });
}

window.onload = renderTasks;

const addTask = (event) => {
    event.preventDefault();

    const task = taskInput.value;
    const taskItem = createTaskItem(task);
    taskList.insertAdjacentHTML("beforeend", taskItem);

    storedTasks.push(task);
    localStorage.setItem("tasks", JSON.stringify(storedTasks));

    addTaskForm.reset();
}

addTaskForm.addEventListener("submit", addTask);

const toggleTaskCompletion = (event) => {
    const taskItem = event.target.parentElement;
    const task = taskItem.querySelector("label");

    if (event.target.checked){
        task.style.textDecoration = "line-through";
    } else{
        task.style.textDecoration = "none";
    }
}

const removeTask = (event) => {
    const taskItem = event.target.parentElement;
    const task = taskItem.querySelector("label").innerText;
    const indexOfTask = storedTasks.indexOf(task);

    storedTasks.splice(indexOfTask, 1);
    localStorage.setItem("tasks", JSON.stringify(storedTasks));

    taskItem.remove();
}

const clearAllTasks = () => {
    const taskItem = target.parentElement;
    const task = taskItem.querySelector("#taskList");
    taskList.remove();
}