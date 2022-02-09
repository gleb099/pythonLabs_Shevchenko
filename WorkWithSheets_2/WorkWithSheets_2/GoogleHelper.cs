using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Google.Apis.Auth.OAuth2;
using Google.Apis.Drive.v3;
using Google.Apis.Sheets.v4;
using Google.Apis.Util.Store;

namespace WorkWithSheets_2
{
    internal class GoogleHelper
    {
        private readonly string token;
        private readonly string sheetFileName;
        private UserCredential credentials;
        private DriveService driveService;
        private SheetsService sheetService;
        private string sheetFileId;
        private string sheetName;

        public GoogleHelper(string token, string sheetFileName)
        {
            this.token = token;
            this.sheetFileName = sheetFileName;
        }

        public string ApplicationName { get; private set; } = "WorkWithSheet";
        public string[] Scopes { get; private set; } = new string[]
        {
            DriveService.Scope.Drive,
            SheetsService.Scope.Spreadsheets
        };

        internal void Set(string cellName, string value)
        {
            var range = this.sheetName + "!" + cellName + ":" + cellName;
            var values = new List<List<object>>
            {
                new List<object> { value }
            };

            var request = this.sheetService.Spreadsheets.Values.Update(
                new Google.Apis.Sheets.v4.Data.ValueRange { Values = new List<IList<object>>(values) },
                spreadsheetId: this.sheetFileId,
                range: range
                );
            request.ValueInputOption = SpreadsheetsResource.ValuesResource.UpdateRequest.ValueInputOptionEnum.USERENTERED;
            var response = request.Execute();
        }

        internal string Get(string cellName)
        {
            var range = this.sheetName + "!" + cellName + ":" + cellName;

            var request = this.sheetService.Spreadsheets.Values.Get(
                spreadsheetId: this.sheetFileId,
                range: range
                );

            var response = request.Execute();
            return response.Values?.First()?.First()?.ToString();
        }

        internal async Task<bool> Start()
        {
            string credentialsPath = Path.Combine(Environment.CurrentDirectory, "credentials", ApplicationName);

            using (var stream = new FileStream("credentials.json", FileMode.Open, FileAccess.Read))
            {
                string credPath = "token.json";
                this.credentials = GoogleWebAuthorizationBroker.AuthorizeAsync(
                    GoogleClientSecrets.Load(stream).Secrets,
                    Scopes,
                    "user",
                    CancellationToken.None,
                    new FileDataStore(credPath, true)).Result;
                Console.WriteLine("Credential file saved to: " + credPath);
            }

            this.driveService = new DriveService(new Google.Apis.Services.BaseClientService.Initializer
            {
                HttpClientInitializer = this.credentials,
                ApplicationName = ApplicationName,
            });

            this.sheetService = new SheetsService(new Google.Apis.Services.BaseClientService.Initializer
            {
                HttpClientInitializer = this.credentials,
                ApplicationName = ApplicationName,
            });

            var request = this.driveService.Files.List();
            var response = request.Execute();

            foreach (var file in response.Files)
            {
                if (file.Name == this.sheetFileName)
                {
                    this.sheetFileId = file.Id;
                    break;
                }
            }

            if (!string.IsNullOrEmpty(this.sheetFileId))
            {
                var sheetRequest = this.sheetService.Spreadsheets.Get(this.sheetFileId);
                var sheetResponse = sheetRequest.Execute();

                this.sheetName = sheetResponse.Sheets[0].Properties.Title;

                return true;
            }
            else return false;
        }
    }
}
