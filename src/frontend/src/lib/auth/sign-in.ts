import { AuthApiCore } from '@/api';
import { CredentialStorage } from '@/assets';
import { authApi } from '@/assets/config/api';
import { TokenPair } from '@/entities';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';
import toast from 'react-hot-toast';
import { useNavigate } from 'react-router-dom';
import { isWrongResponse } from '../typeguard';

interface LoginData {
  email: string;
  password: string;
}

interface SignUpData {
  email: string;
  username: string;
  password: string;
}

export const useSignIn = () => {
  const navigate = useNavigate();

  return useMutation({
    mutationFn: async (credentials: LoginData) => {
      const tokenPair = await axios.post<TokenPair>(`${authApi}/sign-in`, {
        email: credentials.email,
        password: credentials.password,
      });

      if (isWrongResponse(tokenPair)) {
        return null;
      }

      CredentialStorage.set('access', tokenPair.data.access);
      CredentialStorage.set('refresh', tokenPair.data.refresh);

      return tokenPair;
    },
    onError: () => {
      return toast.error('Неверные данные');
    },
    onSuccess: () => {
      toast.success('Успешно!');
      return navigate('/admin/events');
    },
  });
};

export const useSignUp = () => {
  const navigate = useNavigate();

  return useMutation({
    mutationFn: async (credentials: SignUpData) => {
      const tokenPair = await AuthApiCore.signUp({
        email: credentials.email,
        password: credentials.password,
      });

      if (isWrongResponse(tokenPair)) {
        return null;
      }

      CredentialStorage.set('access', tokenPair.data.access_token);
      CredentialStorage.set('refresh', tokenPair.data.access_token);

      return tokenPair;
    },
    onError: () => {
      return toast.error('Неверные данные');
    },
    onSuccess: () => {
      toast.success('Удачно!');
      return setTimeout(() => {
        return navigate('/');
      }, 1500);
    },
  });
};
