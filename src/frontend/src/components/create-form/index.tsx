import NewStyle from '@/assets/styles/new.module.scss';
import { Button, Input } from '@chakra-ui/react';
// import { PieChart } from '@mui/x-charts';
import { Pie } from '@ant-design/plots';
import React from 'react';
import img from '../../../public/upload.svg';

interface CreateFormProps {}
export const CreateForm: React.FC<CreateFormProps> = () => {
  const [data, setData] = React.useState([]);
  React.useEffect(() => {
    setTimeout(() => {
      setData([
        { type: '分类一', value: 27 },
        { type: '分类二', value: 25 },
        { type: '分类三', value: 18 },
        { type: '分类四', value: 15 },
        { type: '分类五', value: 10 },
        { type: '其他', value: 5 },
      ]);
    }, 1000);
  }, []);
  const config = {
    data,
    angleField: 'value',
    colorField: 'type',
    label: {
      text: 'value',
      style: {
        fontWeight: 'bold',
      },
    },
    legend: {
      color: {
        title: false,
        position: 'right',
        rowPadding: 5,
      },
    },
  };
  return (
    <>
      <div className={NewStyle.conteiner}>
        <div className={NewStyle.conteiner_content}>
          <Input variant='flushed' placeholder='Введите название' />
          <div className={NewStyle.chart}>
            <Pie {...config} width={780} />
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
