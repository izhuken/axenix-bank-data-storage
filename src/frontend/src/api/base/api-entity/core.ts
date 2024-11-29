import { CredentialStorage } from '@/assets';
import { API_SERVER_URL } from '@/assets/config';
import { EntityId, PaginatedResponse, WrongResponse } from '@/entities';
import axios, { AxiosError, AxiosRequestConfig, AxiosResponse } from 'axios';

export class EntityAPICore<FetchType, RequestType> {
  public url;
  constructor(prefix: string) {
    this.url = `${API_SERVER_URL}/${prefix}`;
  }

  async fetchAll(
    RequestConfig: AxiosRequestConfig = {},
  ): Promise<AxiosResponse<PaginatedResponse<FetchType>> | WrongResponse> {
    const requestConfig = this.setAuthenticationHeader(RequestConfig);
    return await axios
      .get<PaginatedResponse<FetchType>>(`${this.url}/get_all`, requestConfig)
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }

  async fetchByID(
    id: EntityId,
    RequestConfig: AxiosRequestConfig = {},
  ): Promise<AxiosResponse<FetchType> | WrongResponse> {
    const requestConfig = this.setAuthenticationHeader(RequestConfig);
    return await axios
      .get<FetchType>(`${this.url}/${id}`, requestConfig)
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }

  async create(
    data: RequestType,
    RequestConfig: AxiosRequestConfig = {},
  ): Promise<AxiosResponse<FetchType> | WrongResponse> {
    const requestConfig = this.setAuthenticationHeader(RequestConfig);
    return await axios
      .post<FetchType>(`${this.url}/create`, data, requestConfig)
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }

  async update(
    id: EntityId,
    data: Partial<RequestType>,
    RequestConfig: AxiosRequestConfig = {},
  ): Promise<AxiosResponse<FetchType> | WrongResponse> {
    const requestConfig = this.setAuthenticationHeader(RequestConfig);
    return await axios
      .patch<FetchType>(`${this.url}/update/${id}`, data, requestConfig)
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }

  async remove(
    id: EntityId,
    RequestConfig: AxiosRequestConfig = {},
  ): Promise<AxiosResponse<FetchType> | WrongResponse> {
    const requestConfig = this.setAuthenticationHeader(RequestConfig);
    return await axios
      .delete<FetchType>(`${this.url}/delete/${id}`, requestConfig)
      .catch<WrongResponse>((error: AxiosError) => {
        const response: WrongResponse = {
          code: error.response!.status,
          details: error.response!.data as string,
        };
        return response;
      });
  }

  setAuthenticationHeader(RequestConfig: AxiosRequestConfig) {
    const token = CredentialStorage.get('access');

    if (!token) {
      return RequestConfig;
    }

    const headerValue = `Bearer ${token}`;

    if (!RequestConfig.headers) {
      RequestConfig['headers'] = {};
    }

    RequestConfig.headers['Authorization'] = headerValue;

    return RequestConfig;
  }
}
