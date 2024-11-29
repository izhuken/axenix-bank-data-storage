import { AuthStyles, DefaultButton, DefaultInput } from '@/assets';
import { useSignUp } from '@/lib';
import { FC } from 'react';
import { useForm } from 'react-hook-form';
import { Toaster } from 'react-hot-toast';
import { FormBaseLayout } from '../form-base-layout';

interface SignUpData {
  username: string;
  email: string;
  password: string;
}

export const SignUpLayout: FC = () => {
  const methods = useForm<SignUpData>();
  const { mutate: signUp, isPending } = useSignUp();

  return (
    <article className={AuthStyles.authForm}>
      <h2>Регистрация</h2>
      <FormBaseLayout
        methods={methods}
        onSub={(data: SignUpData) => signUp(data)}
      >
        <DefaultInput
          name='email'
          placeholder='Email'
          registerOptions={{
            required: {
              value: true,
              message: 'Обязательное поле',
            },
            pattern: {
              value: /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/,
              message: 'Неверный формат email',
            },
          }}
        />
        <DefaultInput
          name='username'
          placeholder='Nick name'
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
        <DefaultButton isLoading={isPending} type='submit'>
          Регистрация
        </DefaultButton>
      </FormBaseLayout>
      <Toaster />
    </article>
  );
};
