SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SubjectDemographic](
	[SubjectFirstName] [nvarchar](255) NULL,
	[SubjectLastName] [nvarchar](255) NULL,
	[SubjectGender] [nvarchar](2) NULL,
	[SubjectBirthdate] [nvarchar](20) NULL,
	[SubjectId] [nvarchar](255) NOT NULL,
	[SubjectCity] [nvarchar](50) NULL,
	[SubjectZipcode] [nvarchar](10) NULL,
	[SubjectState] [nvarchar](50) NULL
) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
ALTER TABLE [dbo].[SubjectDemographic] ADD PRIMARY KEY CLUSTERED 
(
	[SubjectId] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF) ON [PRIMARY]
GO