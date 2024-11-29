import { API_SERVER_URL } from '@/assets/config';
import {
  AccessToken,
  ISignIn,
  ISignUp,
  TokenPair,
  User,
  WrongResponse,
} from '@/entities';
import axios, { AxiosError, AxiosResponse } from 'axios';

class _Auth {
  public url: string;

  constructor() {
    this.url = `${API_SERVER_URL}/auth`;
  }

  async signIn(
    data: ISignIn,
  ): Promise<AxiosResponse<TokenPair> | WrongResponse> {
    return await axios
      .post<TokenPair>(`${this.url}/sign-in`, data)
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }

  async signUp(
    data: ISignUp,
  ): Promise<AxiosResponse<TokenPair> | WrongResponse> {
    return await axios
      .post<TokenPair>(`${this.url}/sign-up`, data)
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }

  async refresh(
    data: string,
  ): Promise<AxiosResponse<AccessToken> | WrongResponse> {
    return await axios
      .post<AccessToken>(`${this.url}/refresh-token`, { refresh_token: data })
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }

  async userByToken(
    token: string = '',
  ): Promise<AxiosResponse<User> | WrongResponse> {
    return await axios
      .get<User>(`${this.url}/user`, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }
}

export const AuthApiCore = new _Auth();
