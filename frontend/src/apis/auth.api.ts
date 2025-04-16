import { createApi } from "@reduxjs/toolkit/query/react";
import baseQuery from "./base.query";

export const authApi = createApi({
  reducerPath: "authApi",
  baseQuery,
  endpoints: (builder) => ({
    login: builder.mutation<
      { token: string },
      { email: string; password: string }
    >({
      query: (credentials) => ({
        url: "/login",
        method: "POST",
        body: credentials,
      }),
    }),
    getMe: builder.query<unknown, void>({
      query: () => "/me",
    }),
    getAllUsers: builder.query<unknown[], void>({
      query: () => "/users",
    }),
  }),
});

export const { useLoginMutation, useGetMeQuery, useGetAllUsersQuery } = authApi;
