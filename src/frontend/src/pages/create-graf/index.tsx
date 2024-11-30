import { ChoiseGrafModal } from '@/components/choise-graf';
import { CreateForm } from '@/components/create-form';
import { FormBaseLayout } from '@/components/form-base-layout';
import { Header } from '@/components/header';
import React from 'react';
import { useForm } from 'react-hook-form';
import NewStyle from '../../assets/styles/new.module.scss';

interface CreateGrafProps {}

export type ChartFormData = {
  chartType: 'pie' | 'area' | 'column';
  payload: { value: number; title: string }[];
};

export const CreateGraf: React.FC<CreateGrafProps> = () => {
  const form = useForm<ChartFormData>({
    defaultValues: {
      chartType: 'pie',
    },
  });

  return (
    <>
      <FormBaseLayout
        methods={form}
        onSub={(data) => {
          console.log(data);
        }}
      >
        <Header />
        <div className={NewStyle.conteiner_create}>
          <div className={NewStyle.conteiner_create__content}>
            <div className={NewStyle.conteiner_create__choice}>
              <ChoiseGrafModal />
            </div>

            <CreateForm isActive />
          </div>
        </div>
      </FormBaseLayout>
    </>
  );
};
