
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[hkdata](
	[quantity] [nvarchar](50) NULL,
	[quantityUnit] [nvarchar](50) NULL,
	[startTime] [nvarchar](50) NULL,
	[endTime] [nvarchar](50) NULL,
	[quantityType] [nvarchar](80) NULL,
	[guid] [nvarchar](80) NULL
) ON [PRIMARY]
GO
