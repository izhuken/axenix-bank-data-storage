export type AppEcologyPoint = {
  title: string;
  longitude: string;
  latitude: string;
  address: string;
  is_hidden: boolean;
  id: string;
  create_time: string;
  update_time: string;
  file: {
    point_id: string;
    fraction_id: string;
    id: string;
    url: string;
    create_time: string;
  };
  fraction: [
    {
      title: string;
      description: string;
      is_hidden: boolean;
      id: string;
      create_time: string;
      update_time: string;
    },
  ];
};
