export interface CredentialOptions {
  expires?: Date | string;
  maxAge?: number;
  secure?: boolean;
  samesite?: 'strict' | 'lax';

  httpOnly?: boolean;
}
