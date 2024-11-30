import { ChoiseGrafModal } from '@/components/choise-graf';
import { CreateForm } from '@/components/create-form';
import { Header } from '@/components/header';
import React from 'react';
import NewStyle from '../../assets/styles/new.module.scss';

interface CreateGrafProps {}
export const CreateGraf: React.FC<CreateGrafProps> = () => {
  return (
    <>
      <Header />
      <div className={NewStyle.conteiner_create}>
        <div className={NewStyle.conteiner_create__content}>
          <div className={NewStyle.conteiner_create__choice}>
            <ChoiseGrafModal />
          </div>

          <CreateForm />
        </div>
      </div>
    </>
  );
};
