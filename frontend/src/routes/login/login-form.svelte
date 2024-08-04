<script lang="ts">
	import { goto } from '$app/navigation';

	import { superForm, defaults } from 'sveltekit-superforms';
	import { zod } from 'sveltekit-superforms/adapters';
	import Cookies from 'js-cookie';

	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';

	import { client, schemas } from '$lib/api';

	const form = superForm(defaults(zod(schemas.AuthData)), {
		SPA: true,
		validators: zod(schemas.AuthData),
		onUpdate: async ({ form }) => {
			if (form.valid) {
				const result = await client.login(form.data);
				Cookies.set('token', result.access_token);
				await goto('/');
			}
		}
	});

	const { form: formData, enhance } = form;
</script>

<form use:enhance>
	<Form.Field {form} name="email">
		<Form.Control let:attrs>
			<Form.Label>E-Mail</Form.Label>
			<Input {...attrs} bind:value={$formData.email} />
		</Form.Control>
		<Form.Description>Your email address</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Field {form} name="password">
		<Form.Control let:attrs>
			<Form.Label>Password</Form.Label>
			<Input type="password" {...attrs} bind:value={$formData.password} />
		</Form.Control>
		<Form.Description>Your password</Form.Description>
		<Form.FieldErrors />
	</Form.Field>
	<Form.Button>Login</Form.Button>
</form>
