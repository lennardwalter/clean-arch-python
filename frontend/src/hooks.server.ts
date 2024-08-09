import type { HandleFetch, Handle } from '@sveltejs/kit';

export const handleFetch: HandleFetch = ({ event, request, fetch }) => {
	const token = event.cookies.get('token');
	if (token) {
		request.headers.set('Authorization', `Bearer ${token}`);
	}
	return fetch(request);
};

export const handle: Handle = ({ event, resolve }) =>
	resolve(event, {
		filterSerializedResponseHeaders(name, value) {
			if (name === 'content-type') return true;
			else return false;
		}
	});
