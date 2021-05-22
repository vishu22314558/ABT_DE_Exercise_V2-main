SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SubjectProgram](
	[AccelerometerId] [int] IDENTITY(1,1) NOT NULL,
	[SubjectId] [nvarchar](255) NOT NULL,
	[ProgramName] [nvarchar](255) NOT NULL,
	[Amplitude] [nvarchar](20) NULL,
	[Frequency] [nvarchar](20) NULL,
	[Pulse] [nvarchar](20) NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[SubjectProgram] ADD PRIMARY KEY CLUSTERED 
(
	[AccelerometerId] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[SubjectProgram]  WITH CHECK ADD FOREIGN KEY([SubjectId])
REFERENCES [dbo].[SubjectDemographic] ([SubjectId])
GO
