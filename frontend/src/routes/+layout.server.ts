import { redirect } from '@sveltejs/kit';

import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ url, cookies }) => {
	const token = cookies.get('token');

	if (!token && !url.pathname.includes('login')) {
		redirect(302, '/login');
	}
};
