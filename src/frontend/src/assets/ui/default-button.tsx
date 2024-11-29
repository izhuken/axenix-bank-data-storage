import clsx, { ClassValue } from 'clsx';
import { FC, ReactNode } from 'react';
import { DefaultStyle, Loader } from '..';

type DefaultButtonProps = {
  children?: ReactNode | string;
  style?: 'light' | 'l' | 'dark' | 'd';
  className?: ClassValue;
  isLoading?: boolean;
} & JSX.IntrinsicElements['button'];

export const DefaultButton: FC<DefaultButtonProps> = ({
  isLoading,
  children,
  style,
  className,
  ...other
}) => {
  return (
    <button
      {...other}
      className={clsx(
        DefaultStyle.buttonDefault,
        className ??
          (style === 'l' || style === 'light' ? DefaultStyle.white : ''),
      )}
    >
      {isLoading ? (
        <Loader inverse={!(style === 'l' || style === 'light')} />
      ) : (
        children
      )}
    </button>
  );
};
