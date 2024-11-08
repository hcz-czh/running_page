interface ISiteMetadataResult {
  siteTitle: string;
  siteUrl: string;
  description: string;
  logo: string;
  navLinks: {
    name: string;
    url: string;
  }[];
}

const data: ISiteMetadataResult = {
  siteTitle: 'Hcz\'sRunning Page',
  siteUrl: 'https://run.hechunzhu.com',
  logo: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTtc69JxHNcmN1ETpMUX4dozAgAN6iPjWalQ&usqp=CAU',
  description: 'Hcz\'s running page and blog',
  navLinks: [
    {
      name: 'Blog',
      url: 'blog.hechunzhu.com',
    },
    {
      name: 'About',
      url: 'blog.hechunzhu.com/about',
    },
  ],
};

export default data;
