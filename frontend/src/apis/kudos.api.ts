import { createApi } from "@reduxjs/toolkit/query/react";
import baseQuery from "./base.query";

export const kudosApi = createApi({
  reducerPath: "kudosApi",
  tagTypes: ["GetKudos"],
  baseQuery,
  endpoints: (builder) => ({
    sendKudos: builder.mutation<
      unknown,
      { kudos_to: string; kudos_text: string }
    >({
      query: (data) => ({
        url: "/send-kudos",
        method: "POST",
        body: data,
      }),
      invalidatesTags: ["GetKudos"],
    }),
    getKudos: builder.query<unknown, void>({
      query: () => "/get-kudos",
      providesTags: ["GetKudos"],
    }),
  }),
});

export const { useSendKudosMutation, useGetKudosQuery } = kudosApi;
