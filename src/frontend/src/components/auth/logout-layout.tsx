import { AuthStyles, CredentialStorage, DefaultButton } from '@/assets';
import React from 'react';
import toast, { Toaster } from 'react-hot-toast';
import { useNavigate } from 'react-router-dom';

interface LogoutLayoutProps {}

export const LogoutLayout: React.FC<LogoutLayoutProps> = () => {
  const navigate = useNavigate();

  const logout = () => {
    toast.success('Удачно!');
    return setTimeout(() => {
      CredentialStorage.invalidate();
      return navigate('/');
    }, 1500);
  };

  return (
    <article className={AuthStyles.authForm}>
      <h2>Вы действительно хотите выйти?</h2>
      <DefaultButton
        isLoading={true}
        style={'l'}
        onClick={logout}
        type='button'
      >
        Да
      </DefaultButton>
      <Toaster />
    </article>
  );
};
