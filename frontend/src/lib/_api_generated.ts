import { makeApi } from '@zodios/core';
import { z } from 'zod';




export const TodoResponse = z.object({ id: z.string(), text: z.string(), completed: z.boolean() }).passthrough();
export const TodoCreateRequest = z.object({ text: z.string() }).passthrough();
export const ValidationError = z.object({ loc: z.array(z.union([z.string(), z.number()])), msg: z.string(), type: z.string() }).passthrough();
export const HTTPValidationError = z.object({ detail: z.array(ValidationError) }).partial().passthrough();
export const TodoUpdateRequest = z.object({ text: z.union([z.string(), z.null()]), completed: z.union([z.boolean(), z.null()]) }).partial().passthrough();
export const PasswordStr = z.string();
export const AuthData = z.object({ email: z.string().email(), password: PasswordStr.min(8).max(50).regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).*$/) }).passthrough();
export const Token = z.object({ access_token: z.string(), token_type: z.string() }).passthrough();

export const schemas = {
	TodoResponse,
	TodoCreateRequest,
	ValidationError,
	HTTPValidationError,
	TodoUpdateRequest,
	PasswordStr,
	AuthData,
	Token,
};

export const endpoints = makeApi([
	{
		method: "post",
		path: "/auth/login",
		alias: "login",
		requestFormat: "json",
		parameters: [
			{
				name: "body",
				type: "Body",
				schema: AuthData
			},
		],
		response: Token,
		errors: [
			{
				status: 401,
				description: `Unauthorized`,
				schema: z.void()
			},
			{
				status: 422,
				description: `Validation Error`,
				schema: HTTPValidationError
			},
		]
	},
	{
		method: "get",
		path: "/users/@me/todos",
		alias: "getMyTodos",
		requestFormat: "json",
		response: z.array(TodoResponse),
		errors: [
			{
				status: 401,
				description: `Unauthorized`,
				schema: z.void()
			},
			{
				status: 500,
				description: `Internal Server Error`,
				schema: z.void()
			},
		]
	},
	{
		method: "post",
		path: "/users/@me/todos",
		alias: "createTodo",
		requestFormat: "json",
		parameters: [
			{
				name: "body",
				type: "Body",
				schema: z.object({ text: z.string() }).passthrough()
			},
		],
		response: TodoResponse,
		errors: [
			{
				status: 401,
				description: `Unauthorized`,
				schema: z.void()
			},
			{
				status: 422,
				description: `Validation Error`,
				schema: HTTPValidationError
			},
			{
				status: 500,
				description: `Internal Server Error`,
				schema: z.void()
			},
		]
	},
	{
		method: "patch",
		path: "/users/@me/todos/:todo_id",
		alias: "updateTodo",
		requestFormat: "json",
		parameters: [
			{
				name: "body",
				type: "Body",
				schema: TodoUpdateRequest
			},
			{
				name: "todo_id",
				type: "Path",
				schema: z.string()
			},
		],
		response: TodoResponse,
		errors: [
			{
				status: 401,
				description: `Unauthorized`,
				schema: z.void()
			},
			{
				status: 422,
				description: `Validation Error`,
				schema: HTTPValidationError
			},
			{
				status: 500,
				description: `Internal Server Error`,
				schema: z.void()
			},
		]
	},
	{
		method: "delete",
		path: "/users/@me/todos/:todo_id",
		alias: "deleteTodo",
		requestFormat: "json",
		parameters: [
			{
				name: "todo_id",
				type: "Path",
				schema: z.string()
			},
		],
		response: z.void(),
		errors: [
			{
				status: 401,
				description: `Unauthorized`,
				schema: z.void()
			},
			{
				status: 422,
				description: `Validation Error`,
				schema: HTTPValidationError
			},
			{
				status: 500,
				description: `Internal Server Error`,
				schema: z.void()
			},
		]
	},
]);
