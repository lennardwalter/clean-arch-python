import { redirect } from '@sveltejs/kit';

import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ url, cookies }) => {
	if (!url.pathname.includes('login') && !cookies.get('token')) {
		throw redirect(302, '/login');
	} else if (!url.pathname.includes('todos') && !url.pathname.includes('login')) {
		throw redirect(302, '/todos');
	}
};
