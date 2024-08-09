import type { LoadEvent } from '@sveltejs/kit';

import Cookies from 'js-cookie';
import { Zodios, type ZodiosInstance } from '@zodios/core';
import { pluginFetch } from '@zodios/plugins';

import { browser } from '$app/environment';
import { endpoints, schemas } from './_api_generated';

export { schemas };

const BASE_URL = 'http://127.0.0.1:8000';

const addTokenFromCookiesPlugin = {
	request: async (api, config) => {
		const token = Cookies.get('token') || '';
		return {
			...config,
			headers: {
				...config.headers,
				Authorization: `Bearer ${token}`
			}
		};
	}
};

// api client to inject into load function (which could potentially be run on the server)
// this is used so we can take full advantage of SSR with hydration without refetching etc.
export function injectApi<T>(
	wrapped: (event: LoadEvent & { api: ZodiosInstance<typeof endpoints> }) => T
) {
	return (event: LoadEvent) => {
		const api = new Zodios(BASE_URL, endpoints);

		// use sveltekit fetch to make requests
		// reason: client hydration then can extract the data from site data instead of refetching
		// on the server we add the auth token in the handleFetch hook
		api.use(
			pluginFetch({
				fetch: event.fetch
			})
		);

		// however load can also be run on the client, without prior SSR
		// so we need to add the token from cookies here as well
		api.use(addTokenFromCookiesPlugin);

		return wrapped({ ...event, api });
	};
}

// api client to be only used in the browser in components at runtime
const apiClient = new Zodios(BASE_URL, endpoints);
apiClient.use(addTokenFromCookiesPlugin);

export function getApi() {
	if (!browser) {
		throw new Error(
			'getApi() is only available in the browser, on the server (during SSR) use injectApi() in load function'
		);
	}

	return apiClient;
}
