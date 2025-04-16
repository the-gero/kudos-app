import { configureStore } from "@reduxjs/toolkit";
import { authApi } from "./apis/auth.api";
import { kudosApi } from "./apis/kudos.api";

export const store = configureStore({
  reducer: {
    [authApi.reducerPath]: authApi.reducer,
    [kudosApi.reducerPath]: kudosApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(authApi.middleware, kudosApi.middleware),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
