import { injectApi } from '$lib/api';

export const load = injectApi(async ({ api }) => {
	const todos = await api.getMyTodos();
	return { todos };
});
