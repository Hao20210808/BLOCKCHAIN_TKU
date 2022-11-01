import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { systemApi } from '../../api'

export const login = createAsyncThunk(
  'user/login',
  async (data, { rejectWithValue }) => {
    try {
      const response = await systemApi.user.login(data)
      return response
    } catch (e) {
      return rejectWithValue(e)
    }
  }
)

export const registry = createAsyncThunk(
  'user/registry',
  async (data, { rejectWithValue }) => {
    try {
      const response = await systemApi.user.registry(data)
      return response
    } catch (e) {
      return rejectWithValue(e)
    }
  }
)

export const getUser = createAsyncThunk(
  'user/getUser',
  async (_, { rejectWithValue }) => {
    try {
      const response = await systemApi.user.get()
      return response
    } catch (e) {
      return rejectWithValue(e)
    }
  }
)

const initialState = {
  loading: false,
  error: null,
  loginFlag: false,
  logoutFlag: false,
  registryFlag: false,
  token: '',
  user: null
}

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setToken(state, action) {
      state.token = action.payload;
    },
    removeToken(state) {
      state.token = null;
      localStorage.removeItem('token');
    },
    removeError(state, _) {
      state.errorCode = null;
    },
    setLoginFlag(state, action) {
      state.loginFlag = action.payload;
    },
    setLogoutFlag(state, action) {
      state.logoutFlag = action.payload;
    },
    setRegistryFlag(state, action) {
      state.registryFlag = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(login.pending, (state, _) => {
      state.loading = true;
      state.error = null;
    })
    builder.addCase(login.fulfilled, (state, action) => {
      const { token } = action.payload;
      state.loading = false;
      state.token = token;
      state.loginFlag = true;
      localStorage.setItem('token', token);
    })
    builder.addCase(login.rejected, (state, action) => {
      state.loading = false;
      state.error = action.payload;
    })
    builder.addCase(registry.pending, (state, _) => {
      state.loading = true;
      state.error = null;
    })
    builder.addCase(registry.fulfilled, (state, _) => {
      state.loading = false;
      state.token = null;
      state.registryFlag = true;
      localStorage.removeItem('token');
    })
    builder.addCase(registry.rejected, (state, action) => {
      state.loading = false;
      state.error = action.payload;
    })
    builder.addCase(getUser.pending, (state, _) => {
      state.loading = true;
      state.error = null;
    })
    builder.addCase(getUser.fulfilled, (state, action) => {
      state.loading = false;
      state.user = action.payload.user;
    })
    builder.addCase(getUser.rejected, (state, action) => {
      state.loading = false;
      state.error = action.payload;
    })
  },
})

const { actions, reducer } = userSlice

export const {
    setToken,
    removeError,
    removeToken,
    setLoginFlag,
    setRegistryFlag,
    setLogoutFlag
} = actions

export default reducer