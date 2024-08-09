<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Input } from '$lib/components/ui/input';

	import { getApi } from '$lib/api';

	const { data } = $props();

	// TODO: do we have to do that? how does svelte 5 even work???
	let todos = $state(data.todos);

	let newTodoText = $state('');

	async function createTodo() {
		const todo = await getApi().createTodo({
			text: newTodoText
		});
		todos.push(todo);
		newTodoText = '';
	}

	async function remove(id: string) {
		await getApi().deleteTodo(undefined, { params: { todo_id: id } });
		todos = todos.filter((todo) => todo.id !== id);
	}

	async function toggleComplete(id: string) {
		const todo = todos.find((todo) => todo.id === id);
		if (!todo) return;
		await getApi().updateTodo(
			{
				completed: !todo.completed
			},
			{ params: { todo_id: id } }
		);
		todo.completed = !todo.completed;
	}
</script>

<main class="flex h-screen flex-col items-center justify-center gap-4">
	<h1 class="text-4xl">Todos</h1>

	<div class="flex gap-2">
		<Input type="text" bind:value={newTodoText} placeholder="New todo text" />
		<Button on:click={createTodo}>Create</Button>
	</div>

	<ul class="flex flex-col gap-2">
		{#each todos as todo}
			<li class="flex items-center gap-2">
				<Checkbox checked={todo.completed} onCheckedChange={() => toggleComplete(todo.id)} />
				<span class={todo.completed ? 'line-through' : ''}>{todo.text}</span>
				<Button on:click={() => remove(todo.id)}>Remove</Button>
			</li>
		{/each}
	</ul>
</main>
