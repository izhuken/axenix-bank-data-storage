import { HomepageStyles } from '@/assets';
import { Header } from '@/components';
import { Button } from '@chakra-ui/react';
import React from 'react';

interface HomepageProps {}

export const Homepage: React.FC<HomepageProps> = () => {
  // const navigate = useNavigate();

  // useEffect(() => {
  //   navigate('/login');
  // }, []);

  return (
    <>
      <Header />
      <div className={HomepageStyles.homapageContainer}>
        <div className={HomepageStyles.homapageText}>
          <p className={HomepageStyles.homapageTitle}>
            Место, где идеи становятся реальностью
          </p>
          <p className={HomepageStyles.homapageContent}>
            Наш подход к работе основан на глубоком понимании потребностей
            клиента, тщательном анализе рынка и создании уникальных решений,
            которые помогут достичь поставленных целей.
          </p>
          {/* <DefaultButton
            onClick={() => {
              navigate('/sign-in', { replace: true });
            }}
          >
            Перейти
          </DefaultButton> */}
          <Button background='rgba(255, 86, 2, 1)' color='black' width={400}>
            Перейти
          </Button>
        </div>
        <div className={HomepageStyles.imageContainer}>
          <img src='/home-preview.svg' alt='' width={450} />
        </div>
      </div>
    </>
  );
};
