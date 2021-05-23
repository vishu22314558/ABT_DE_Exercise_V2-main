

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[locdata](
	[latitude] [nvarchar](50) NULL,
	[longitude] [nvarchar](50) NULL,
	[time] [nvarchar](50) NULL,
	[altitude] [nvarchar](50) NULL,
	[guid] [nvarchar](80) NULL
) ON [PRIMARY]
GO