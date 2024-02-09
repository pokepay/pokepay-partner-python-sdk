// DO NOT EDIT: File is generated by code generator.

import { Request, Method } from "./Request";
import { PaginatedAccountBalance } from "../response/PaginatedAccountBalance";

class ListAccountExpiredBalances implements Request<PaginatedAccountBalance> {
  public readonly __r: PaginatedAccountBalance | undefined;
  public readonly method: Method = "GET";
  public readonly path: string;
  public readonly bodyParams: {
    page?: number,
    per_page?: number,
    expires_at_from?: string,
    expires_at_to?: string,
    direction?: string
  };
  public constructor(params: {
    account_id: string,
    page?: number,
    per_page?: number,
    expires_at_from?: string,
    expires_at_to?: string,
    direction?: string
  }) {
    if (params.account_id === void 0) throw new Error('"account_id" is required');
    this.path = "/accounts" + "/" + params.account_id + "/expired-balances";
    this.bodyParams = {};
    if (params.page !== void 0) this.bodyParams.page = params.page;
    if (params.per_page !== void 0) this.bodyParams.per_page = params.per_page;
    if (params.expires_at_from !== void 0) this.bodyParams.expires_at_from = params.expires_at_from;
    if (params.expires_at_to !== void 0) this.bodyParams.expires_at_to = params.expires_at_to;
    if (params.direction !== void 0) this.bodyParams.direction = params.direction;
  }
}

export { ListAccountExpiredBalances };
