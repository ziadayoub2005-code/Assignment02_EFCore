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

CREATE TABLE [Authors] (
    [Id] int NOT NULL IDENTITY,
    [Name] nvarchar(100) NOT NULL,
    [BirthDate] datetime2 NOT NULL,
    CONSTRAINT [PK_Authors] PRIMARY KEY ([Id])
);
GO

CREATE TABLE [Borrowers] (
    [Id] int NOT NULL IDENTITY,
    [Name] nvarchar(100) NOT NULL,
    [MembershipDate] datetime2 NOT NULL DEFAULT (GETDATE()),
    CONSTRAINT [PK_Borrowers] PRIMARY KEY ([Id])
);
GO

CREATE TABLE [Books] (
    [Id] int NOT NULL IDENTITY,
    [Title] nvarchar(150) NOT NULL,
    [ISBN] nvarchar(20) NOT NULL,
    [AuthorId] int NOT NULL,
    CONSTRAINT [PK_Books] PRIMARY KEY ([Id]),
    CONSTRAINT [FK_Books_Authors_AuthorId] FOREIGN KEY ([AuthorId]) REFERENCES [Authors] ([Id]) ON DELETE CASCADE
);
GO

CREATE TABLE [Loans] (
    [BookId] int NOT NULL,
    [BorrowerId] int NOT NULL,
    [LoanDate] datetime2 NOT NULL DEFAULT (GETDATE()),
    [ReturnDate] datetime2 NULL,
    CONSTRAINT [PK_Loans] PRIMARY KEY ([BookId], [BorrowerId]),
    CONSTRAINT [FK_Loans_Books_BookId] FOREIGN KEY ([BookId]) REFERENCES [Books] ([Id]) ON DELETE CASCADE,
    CONSTRAINT [FK_Loans_Borrowers_BorrowerId] FOREIGN KEY ([BorrowerId]) REFERENCES [Borrowers] ([Id]) ON DELETE CASCADE
);
GO

CREATE INDEX [IX_Books_AuthorId] ON [Books] ([AuthorId]);
GO

CREATE INDEX [IX_Loans_BorrowerId] ON [Loans] ([BorrowerId]);
GO

INSERT INTO [__EFMigrationsHistory] ([MigrationId], [ProductVersion])
VALUES (N'20261012115309_InitialCreate', N'5.0.17');
GO

COMMIT;
GO

