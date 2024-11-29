import { AuthStyles, DefaultButton, DefaultInput } from '@/assets';
import { useSignIn } from '@/lib';
import React from 'react';
import { useForm } from 'react-hook-form';
import { Toaster } from 'react-hot-toast';
import { FormBaseLayout } from '../form-base-layout';

interface SignInLayoutProps {}

interface SignInData {
  email: string;
  password: string;
}

export const SignInLayout: React.FC<SignInLayoutProps> = () => {
  const methods = useForm<SignInData>();
  const { mutate: signIn, isPending: isSignInLoading } = useSignIn();

  return (
    <article className={AuthStyles.authForm}>
      <h2>Вход</h2>
      <FormBaseLayout
        methods={methods}
        onSub={(data: SignInData) => {
          signIn(data);
        }}
      >
        <DefaultInput
          name='email'
          placeholder='Email'
          registerOptions={{
            required: {
              value: true,
              message: 'Обязательное поле',
            },
          }}
        />
        <DefaultInput
          name='password'
          placeholder='Пароль'
          registerOptions={{
            required: {
              value: true,
              message: 'Обязательное поле',
            },
          }}
        />
        <DefaultButton isLoading={isSignInLoading} type='submit'>
          Войти
        </DefaultButton>
      </FormBaseLayout>
      <Toaster />
    </article>
  );
};
