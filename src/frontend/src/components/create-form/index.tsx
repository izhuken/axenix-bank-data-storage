import NewStyle from '@/assets/styles/new.module.scss';
import { Button, Input } from '@chakra-ui/react';

// import { Column } from '@ant-design/plots';
import { ChartFormData } from '@/pages/create-graf';
import React from 'react';
import { useFormContext } from 'react-hook-form';
import img from '../../../public/upload.svg';
import { AreaChart } from '../charts/area-chart';
import { ColumnChart } from '../charts/column-chart';
import { PieChart } from '../charts/pie-chart';

interface CreateFormProps {
  isActive: boolean;
}

export const CreateForm: React.FC<CreateFormProps> = () => {
  const { watch } = useFormContext<ChartFormData>();
  const chartType = watch('chartType');

  return (
    <>
      <div className={NewStyle.conteiner}>
        <div className={NewStyle.conteiner_content}>
          <Input variant='flushed' placeholder='Введите название' />
          <div className={NewStyle.chart}>
            {chartType === 'pie' && <PieChart />}
            {chartType === 'area' && <AreaChart />}
            {chartType === 'column' && <ColumnChart />}
          </div>
          <hr color='black' />
          <div className={NewStyle.label}>
            <div className={NewStyle.label_load}>
              <img src={img} />
              <p>Скачать график</p>
            </div>
            <div className={NewStyle.label_btn}>
              <Button>PNG</Button>
              <Button>SVG</Button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
