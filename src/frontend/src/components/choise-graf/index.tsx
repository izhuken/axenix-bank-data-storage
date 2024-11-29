import { Area } from '@/assets/styles/area';
import { Column } from '@/assets/styles/column';
import NewStyle from '@/assets/styles/new.module.scss';
import { Pie } from '@/assets/styles/pie';
import { Button } from '@chakra-ui/react';
import React from 'react';

interface ChoiseGrafModalProps {}
export const ChoiseGrafModal: React.FC<ChoiseGrafModalProps> = () => {
  return (
    <>
      <div className={NewStyle.box}>
        <div className={NewStyle.content_box}>
          <p className={NewStyle.title}>Вид графика</p>
          <div className={NewStyle.group}>
            <Button leftIcon={<Pie />} width={300} gap={1}>
              Пирог
            </Button>
            <Button leftIcon={<Column />} width={300} gap={1}>
              Колонны
            </Button>
            <Button leftIcon={<Area />} width={300} gap={1}>
              Области
            </Button>
          </div>
        </div>
      </div>
    </>
  );
};
