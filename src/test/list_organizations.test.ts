// DO NOT EDIT: File is generated by code generator.

import {
  Client,
  VERSION,
  Request,
  Method,
  Response,
  ListOrganizations,
  PaginatedOrganizations,
  SendEcho,
  Echo,
  CreateOrganization,
  Organization,
  UpdateWebhook,
  CreateWebhook,
  OrganizationWorkerTaskWebhook,
  DeleteWebhook,
  ListWebhooks,
  PaginatedOrganizationWorkerTaskWebhook,
} from '../index';

import * as util from './util';

const client = new Client("~/.pokepay/test-config.ini");

test('simple', async () => {
  const response: PaginatedOrganizations = <PaginatedOrganizations>(await client.send(new ListOrganizations({
    private_money_id: "4b138a4c-8944-4f98-a5c4-96d3c1c415eb",
  }))).object;
  console.log(response);
})
test('paging', async () => {
  const response: PaginatedOrganizations = <PaginatedOrganizations>(await client.send(new ListOrganizations({
    private_money_id: "4b138a4c-8944-4f98-a5c4-96d3c1c415eb",

    "per_page": 3,}))).object;
  expect(3).toBe(response.pagination.per_page);
})
