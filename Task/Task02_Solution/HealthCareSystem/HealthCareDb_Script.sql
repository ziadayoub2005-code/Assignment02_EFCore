IF OBJECT_ID(N'[__EFMigrationsHistory]') IS NULL
BEGIN
    CREATE TABLE [__EFMigrationsHistory] (
        [MigrationId] nvarchar(150) NOT NULL,
        [ProductVersion] nvarchar(32) NOT NULL,
        CONSTRAINT [PK___EFMigrationsHistory] PRIMARY KEY ([MigrationId])
    );
END;
GO

BEGIN TRANSACTION;
GO

CREATE TABLE [Doctors] (
    [Id] int NOT NULL IDENTITY,
    [Name] nvarchar(100) NOT NULL,
    [Specialization] nvarchar(100) NOT NULL,
    CONSTRAINT [PK_Doctors] PRIMARY KEY ([Id])
);
GO

CREATE TABLE [Patients] (
    [Id] int NOT NULL IDENTITY,
    [Name] nvarchar(100) NOT NULL,
    [DateOfBirth] datetime2 NOT NULL,
    CONSTRAINT [PK_Patients] PRIMARY KEY ([Id])
);
GO

CREATE TABLE [Appointments] (
    [PatientId] int NOT NULL,
    [DoctorId] int NOT NULL,
    [AppointmentDate] datetime2 NOT NULL,
    CONSTRAINT [PK_Appointments] PRIMARY KEY ([PatientId], [DoctorId], [AppointmentDate]),
    CONSTRAINT [FK_Appointments_Doctors_DoctorId] FOREIGN KEY ([DoctorId]) REFERENCES [Doctors] ([Id]) ON DELETE CASCADE,
    CONSTRAINT [FK_Appointments_Patients_PatientId] FOREIGN KEY ([PatientId]) REFERENCES [Patients] ([Id]) ON DELETE CASCADE
);
GO

CREATE INDEX [IX_Appointments_DoctorId] ON [Appointments] ([DoctorId]);
GO

INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
VALUES (N'20261012115656_InitialCreate', N'5.0.17');
GO

COMMIT;
GO

