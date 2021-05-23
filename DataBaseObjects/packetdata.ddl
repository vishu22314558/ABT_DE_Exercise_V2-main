SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[packetdata](
	[guid] [nvarchar](80) NULL,
	[filename] [nvarchar](100) NULL,
	[packetnumber] [nvarchar](20) NULL,
	[data] [nvarchar](200) NULL
) ON [PRIMARY]
GO


