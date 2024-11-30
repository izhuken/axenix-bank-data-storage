import { Area } from '@/assets/styles/area';
import { Column } from '@/assets/styles/column';
import NewStyle from '@/assets/styles/new.module.scss';
import { Pie } from '@/assets/styles/pie';
import { ChartFormData } from '@/pages/create-graf';
import { Button } from '@chakra-ui/react';
import React from 'react';
import { Controller, useFormContext } from 'react-hook-form';

interface ChoiseGrafModalProps {}
export const ChoiseGrafModal: React.FC<ChoiseGrafModalProps> = () => {
  const { control } = useFormContext<ChartFormData>();

  return (
    <>
      <div className={NewStyle.box}>
        <div className={NewStyle.content_box}>
          <p className={NewStyle.title}>Вид графика</p>
          <div className={NewStyle.group}>
            <Controller
              name='chartType'
              render={({ field: { onChange } }) => (
                <Button
                  onClick={() => onChange('pie')}
                  leftIcon={<Pie />}
                  width={300}
                  gap={1}
                >
                  Пирог
                </Button>
              )}
            />
            <Controller
              name='chartType'
              render={({ field: { onChange } }) => (
                <Button
                  onClick={() => onChange('column')}
                  leftIcon={<Column />}
                  width={300}
                  gap={1}
                >
                  Колонны
                </Button>
              )}
            />
            <Controller
              name='chartType'
              render={({ field: { onChange } }) => (
                <Button
                  onClick={() => onChange('area')}
                  leftIcon={<Area />}
                  width={300}
                  gap={1}
                >
                  Области
                </Button>
              )}
            />
          </div>
        </div>
      </div>
    </>
  );
};
