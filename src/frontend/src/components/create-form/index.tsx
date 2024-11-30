import NewStyle from '@/assets/styles/new.module.scss';
import { Button, Input } from '@chakra-ui/react';

// import { Column } from '@ant-design/plots';
import { Area } from '@ant-design/plots';
import React from 'react';
import img from '../../../public/upload.svg';

interface CreateFormProps {}
export const CreateForm: React.FC<CreateFormProps> = () => {
  //PIE
  // const [data, setData] = React.useState([]);
  // React.useEffect(() => {
  //   setTimeout(() => {
  //     setData([
  //       { type: '分类一', value: 27 },
  //       { type: '分类二', value: 25 },
  //       { type: '分类三', value: 18 },
  //       { type: '分类四', value: 15 },
  //       { type: '分类五', value: 10 },
  //       { type: '其他', value: 5 },
  //     ]);
  //   }, 1000);
  // }, []);
  // const config = {
  //   data,
  //   angleField: 'value',
  //   colorField: 'type',
  //   label: {
  //     text: 'value',
  //     style: {
  //       fontWeight: 'bold',
  //     },
  //   },
  //   legend: {
  //     color: {
  //       title: false,
  //       position: 'right',
  //       rowPadding: 5,
  //     },
  //   },
  // };

  //COLUMN
  // const config = {
  //   data: {
  //     type: 'fetch',
  //     value:
  //       'https://gw.alipayobjects.com/os/antfincdn/iPY8JFnxdb/dodge-padding.json',
  //   },
  //   xField: '月份',
  //   yField: '月均降雨量',
  //   colorField: 'name',
  //   group: true,
  //   style: {
  //     inset: 5,
  //   },
  //   onReady: ({ chart }) => {
  //     try {
  //       chart.on('afterrender', () => {
  //         chart.emit('legend:filter', {
  //           data: { channel: 'color', values: ['London'] },
  //         });
  //       });
  //     } catch (e) {
  //       console.error(e);
  //     }
  //   },
  // };

  const config = {
    data: {
      type: 'fetch',
      value: 'https://assets.antv.antgroup.com/g2/aapl.json',
    },
    xField: (d) => new Date(d.date),
    yField: 'close',
  };

  return (
    <>
      <div className={NewStyle.conteiner}>
        <div className={NewStyle.conteiner_content}>
          <Input variant='flushed' placeholder='Введите название' />
          <div className={NewStyle.chart}>
            {/* <Pie {...config} width={780} /> */}
            {/* <Column {...config} /> */}
            <Area {...config} />
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
