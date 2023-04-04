html_str = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>REPORT</title>
    <style>
      html {
        scroll-behavior: smooth;
      }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <div id="root-div" style="text-align: center">
      <!-- Top Nav bar -->
      <nav
        class="navbar fixed-top bg-dark-subtle shadow-lg p-3 mb-5 bg-body-tertiary"
        data-bs-theme="dark"
      >
        <div class="container-fluid">
          <a class="navbar-brand" style="font-size: x-large;">T E S T -  R E S T - A P I </a>
          <form class="d-flex" role="search">
            <a class="text-light" type="submit" href="https://pypi.org/project/test-rest-api/" target="_blank">
            <img src="https://raw.githubusercontent.com/troymjose/test_rest_api/version_0.0.0.3/test_rest_api.ico" alt="" width="50" height="50" class="rounded-circle"></a>
            </a>
          </form>
        </div>
      </nav>
      <!-- Summary Results -->
      <div id="summary-div" style="padding: 30px; text-align: left">
        <br />
        <br />
        <br />
        <h4 class="text-body-secondary">
          <i class="bi bi-clipboard2-data-fill"></i>&nbsp;&nbsp;Summary
        </h4>
        <hr class="border border-secondary border-2 opacity-50" />
        <div class="row row-cols-1 row-cols-md-4 g-4">
          <div class="col">
            <!-- Run Results -->
            <div class="card h-100">
              <div class="card-header">
                <h5 class="card-title text-body-secondary">
                  <i class="bi bi-speedometer"></i>&nbsp;&nbsp;Run
                </h5>
              </div>
              <div class="card-body">
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Status</td>
                      {% if summary.test.status %}
                      <td>
                        <span
                          class="badge text-bg-light rounded-pill"
                          style="color: #4bc0c0 !important"
                          >PASS</span
                        >
                      </td>
                      {% else %}
                      <td>
                        <span
                          class="badge text-bg-light rounded-pill"
                          style="color: #ff6384 !important"
                          >FAIL</span
                        >
                      </td>
                      {% endif %}
                    </tr>
                    <tr>
                      <td>Tests</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.test.total }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Start</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.test.start }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>End</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.test.end }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Duration</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.test.duration }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Tags</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ '#' + '#'.join(summary.test.tags) if
                          summary.test.tags else '#ALL' }}</span
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="card-footer">
                <canvas id="runDoughnutChart"></canvas>
              </div>
            </div>
          </div>
          <div class="col">
            <!-- Status Results -->
            <div class="card h-100">
              <div class="card-header">
                <h5 class="card-title text-body-secondary">
                  <i class="bi bi-ui-checks-grid"></i>&nbsp;&nbsp;Status
                </h5>
              </div>
              <div class="card-body">
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Total</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.tests.total }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Pass</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.tests.success }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Fail</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.tests.fail }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Error</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.tests.error }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Disable</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.tests.disable }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Skip</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.tests.skip }}</span
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="card-footer">
                <canvas id="statusDoughnutChart"></canvas>
              </div>
            </div>
          </div>
          <div class="col">
            <!-- Status Bugs -->
            <div class="card h-100">
              <div class="card-header">
                <h5 class="card-title text-body-secondary">
                  <i class="bi bi-bug-fill"></i>&nbsp;&nbsp;Bugs
                </h5>
              </div>
              <div class="card-body">
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Total</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.bugs.total }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Low</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.bugs.low }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Minor</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.bugs.minor }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Major</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.bugs.major }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Critical</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.bugs.critical }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Blocker</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.bugs.blocker }}</span
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="card-footer">
                <canvas id="bugDoughnutChart"></canvas>
              </div>
            </div>
          </div>
          <div class="col">
            <!-- Status Errors -->
            <div class="card h-100">
              <div class="card-header">
                <h5 class="card-title text-body-secondary">
                  <i class="bi bi-x-octagon-fill"></i>&nbsp;&nbsp;Errors
                </h5>
              </div>
              <div class="card-body">
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Total</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.errors.total }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Rest Api</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.errors.rest_api }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Global Variables</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.errors.global_variables }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Bug</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.errors.bug }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Logger</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.errors.logger }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Unexpected</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ summary.errors.unexpected }}</span
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="card-footer">
                <canvas id="errorDoughnutChart"></canvas>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Synchronous Tests -->
      <div id="sync-div" style="padding: 30px; text-align: left">
        <br />
        <br />
        <br />
        <nav
          class="navbar bg-body-tertiary"
          style="background-color: white !important"
        >
          <div class="container-fluid">
            <h4 class="text-body-secondary">
              <i class="bi bi-list-ol"></i>&nbsp;&nbsp;Synchronous Tests
            </h4>
            <form class="d-flex" role="search">
              <input
                id="sync_test_search"
                class="form-control me-4"
                type="search"
                placeholder="Search"
              />
              <div
                class="btn-group"
                role="group"
                aria-label="Basic outlined example"
              >
                <button
                  id="sync_test_open_all"
                  type="button"
                  class="btn btn-outline-secondary"
                >
                  <i class="bi bi-arrow-down-circle-fill"></i>
                </button>
                <button
                  id="sync_test_close_all"
                  type="button"
                  class="btn btn-outline-secondary"
                >
                  <i class="bi bi-arrow-up-circle-fill"></i>
                </button>
              </div>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </form>
          </div>
        </nav>
        <hr class="border border-secondary border-2 opacity-50" />
        <!-- Synchronous Test Result Accordion -->
        <div class="accordion" id="syncTestResultAccordion">
          {% for sync_test in sync_tests %}
          <div
            class="accordion-item"
            id="{{ sync_test.name.replace(' ','').replace('(','').replace(')','').replace('[','').replace(']','') }}"
          >
            <h2 class="accordion-header">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-{{ sync_test.name.replace(' ','-').replace('(','').replace(')','').replace('[','').replace(']','') }}"
                aria-expanded="false"
                aria-controls="panelsStayOpen-{{ sync_test.name.replace(' ','-').replace('(','').replace(')','').replace('[','').replace(']','') }}"
              >
                {% if sync_test.status == "pass" %}
                <span class="badge" style="background-color: #4bc0c0"
                  ><i class="bi bi-check-circle-fill"></i>&nbsp;&nbsp;<b
                    >PASS</b
                  ></span
                >&nbsp;&nbsp; {% elif sync_test.status == "fail" %}
                <span class="badge" style="background-color: #ff6384"
                  ><i class="bi bi-bug-fill"></i>&nbsp;&nbsp;<b>FAIL</b></span
                >&nbsp;&nbsp; {% elif sync_test.status == "error" %}
                <span class="badge" style="background-color: #ffcd56"
                  ><i class="bi bi-x-octagon-fill"></i>&nbsp;&nbsp;<b
                    >ERROR</b
                  ></span
                >&nbsp;&nbsp; {% else %}
                <span class="badge" style="background-color: #ffcd56"
                  ><i class="bi bi-x-octagon-fill"></i>&nbsp;&nbsp;<b
                    >ERROR</b
                  ></span
                >&nbsp;&nbsp; {% endif %} {{ sync_test.name }}
              </button>
            </h2>
            <div
              id="panelsStayOpen-{{ sync_test.name.replace(' ','-').replace('(','').replace(')','').replace('[','').replace(']','') }}"
              class="accordion-collapse collapse"
            >
              <div class="accordion-body">
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Name</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ sync_test.name }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Description</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ sync_test.desc }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Asynchronous</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{sync_test.is_async }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Testsuite</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ sync_test.testsuite }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Tags</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ '#' + '#'.join(sync_test.tags) if sync_test.tags
                          else '#ALL' }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Start</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ sync_test.start }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>End</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ sync_test.end }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Duration</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ sync_test.duration }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Bug Priority</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ sync_test.bug_priority }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Error Type</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ sync_test.error_type.replace('_', ' ').title() }}</span
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
                <div class="card">
                  <div class="card-body">
                    <pre>{{ sync_test.details }}</pre>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
      <!-- Asynchronous Tests -->
      <div id="async-div" style="padding: 30px; text-align: left">
        <br />
        <br />
        <br />
        <nav
          class="navbar bg-body-tertiary"
          style="background-color: white !important"
        >
          <div class="container-fluid">
            <h4 class="text-body-secondary">
              <i class="bi bi-list-stars"></i>&nbsp;&nbsp;Asynchronous Tests
            </h4>
            <form class="d-flex" role="search">
              <input
                id="async_test_search"
                class="form-control me-4"
                type="search"
                placeholder="Search"
              />
              <div
                class="btn-group"
                role="group"
                aria-label="Basic outlined example"
              >
                <button
                  id="async_test_open_all"
                  type="button"
                  class="btn btn-outline-secondary"
                >
                  <i class="bi bi-arrow-down-circle-fill"></i>
                </button>
                <button
                  id="async_test_close_all"
                  type="button"
                  class="btn btn-outline-secondary"
                >
                  <i class="bi bi-arrow-up-circle-fill"></i>
                </button>
              </div>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </form>
          </div>
        </nav>
        <hr class="border border-secondary border-2 opacity-50" />
        <!-- Asynchronous Test Result Accordion -->
        <div class="accordion" id="asyncTestResultAccordion">
          {% for async_test in async_tests %}
          <div
            class="accordion-item"
            id="{{ async_test.name.replace(' ','').replace('(','').replace(')','').replace('[','').replace(']','') }}"
          >
            <h2 class="accordion-header">
              <button
                class="accordion-button collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#panelsStayOpen-{{ async_test.name.replace(' ','-').replace('(','').replace(')','').replace('[','').replace(']','') }}"
                aria-expanded="false"
                aria-controls="panelsStayOpen-{{ async_test.name.replace(' ','-').replace('(','').replace(')','').replace('[','').replace(']','') }}"
              >
                {% if async_test.status == "pass" %}
                <span class="badge" style="background-color: #4bc0c0"
                  ><i class="bi bi-check-circle-fill"></i>&nbsp;&nbsp;<b
                    >PASS</b
                  ></span
                >&nbsp;&nbsp; {% elif async_test.status == "fail" %}
                <span class="badge" style="background-color: #ff6384"
                  ><i class="bi bi-bug-fill"></i>&nbsp;&nbsp;<b>FAIL</b></span
                >&nbsp;&nbsp; {% elif async_test.status == "error" %}
                <span class="badge" style="background-color: #ffcd56"
                  ><i class="bi bi-x-octagon-fill"></i>&nbsp;&nbsp;<b
                    >ERROR</b
                  ></span
                >&nbsp;&nbsp; {% else %}
                <span class="badge" style="background-color: #ffcd56"
                  ><i class="bi bi-x-octagon-fill"></i>&nbsp;&nbsp;<b
                    >ERROR</b
                  ></span
                >&nbsp;&nbsp; {% endif %} {{ async_test.name }}
              </button>
            </h2>
            <div
              id="panelsStayOpen-{{ async_test.name.replace(' ','-').replace('(','').replace(')','').replace('[','').replace(']','') }}"
              class="accordion-collapse collapse"
            >
              <div class="accordion-body">
                <table class="table table-hover">
                  <tbody>
                    <tr>
                      <td>Name</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.name }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Description</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.desc }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Asynchronous</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.is_async }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Testsuite</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.testsuite }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Tags</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ '#' + '#'.join(async_test.tags) if async_test.tags
                          else '#ALL' }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Start</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.start }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>End</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.end }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Duration</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.duration }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Bug Priority</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.bug_priority }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>Error Type</td>
                      <td>
                        <span class="badge text-bg-light rounded-pill"
                          >{{ async_test.error_type.replace('_', ' ').title() }}</span
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
                <div class="card">
                  <div class="card-body">
                    <pre>{{ async_test.details }}</pre>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>
    <!-- Floating button for navigating summary, sync & async sections -->
    <div
      class="btn-group-vertical"
      role="group"
      aria-label="Vertical button group"
      style="
        position: fixed;
        bottom: 0;
        right: 0;
        background-color: #ffffff;
        opacity: 0.5;
        z-index: 50;
        border-radius: 50px;
      "
    >
      <a
        role="button"
        class="btn btn-link btn-lg"
        href="#root-div"
        style="text-decoration: none; color: black"
        ><b
          ><i
            class="bi bi-clipboard2-data-fill"
            style="font-size: xx-large"
          ></i></b
      ></a>
      <a
        role="button"
        class="btn btn-link btn-lg"
        href="#sync-div"
        style="text-decoration: none; color: black"
        ><b><i class="bi bi-list-ol" style="font-size: xx-large"></i></b
      ></a>
      <a
        role="button"
        class="btn btn-link btn-lg"
        href="#async-div"
        style="text-decoration: none; color: black"
        ><b><i class="bi bi-list-stars" style="font-size: xx-large"></i></b
      ></a>
    </div>
    <!-- Bootstrap cdn -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-qKXV1j0HvMUeCBQ+QVp7JcfGl760yU08IQ+GpUo5hlbpg51QRiuqHAJz8+BrxE/N"
      crossorigin="anonymous"
    ></script>
    <!-- Chart.js cdn -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Summary Run Doughnut Chart -->
    <script>
      const runDoughnutChart = document.getElementById("runDoughnutChart");
      new Chart(runDoughnutChart, {
        type: "doughnut",
        data: {
          labels: ["Synchronous", "Asynchronous"],
          datasets: [
            {
              label: "Tests",
              data: [{{ summary.tests.sync_tests }}, {{ summary.tests.async_tests }}],
              backgroundColor: [
                "rgba(54, 162, 235, 0.5)",
                "rgba(153, 102, 255, 0.5)",
              ],
              hoverOffset: 4,
            },
          ],
        },
      });
    </script>
    <!-- Summary Status Doughnut Chart -->
    <script>
      const statusDoughnutChart = document.getElementById(
        "statusDoughnutChart"
      );
      new Chart(statusDoughnutChart, {
        type: "doughnut",
        data: {
          labels: ["Pass", "Fail", "Error", "Disable", "Skip"],
          datasets: [
            {
              label: "Status",
              data: [{{ summary.tests.success }}, {{ summary.tests.fail }}, {{ summary.tests.error }}, {{ summary.tests.disable }}, {{ summary.tests.skip }}],
              backgroundColor: [
                "rgba(75, 192, 192,0.8)",
                "rgba(255, 99, 132, 0.8)",
                "rgba(255, 205, 86, 0.8)",
                "rgba(201, 203, 207, 0.8)",
                "rgba(54, 162, 235, 0.8)",
              ],
              hoverOffset: 4,
            },
          ],
        },
      });
    </script>
    <!-- Summary Bug Doughnut Chart -->
    <script>
      const bugDoughnutChart = document.getElementById("bugDoughnutChart");
      new Chart(bugDoughnutChart, {
        type: "doughnut",
        data: {
          labels: ["Low", "Minor", "Major", "Critical", "Blocker"],
          datasets: [
            {
              label: "Priority",
              data: [{{ summary.bugs.low }}, {{ summary.bugs.minor }}, {{ summary.bugs.major }}, {{ summary.bugs.critical }}, {{ summary.bugs.blocker }}],
              backgroundColor: [
                "rgba(255, 99, 132, 0.1)",
                "rgba(255, 99, 132, 0.3)",
                "rgba(255, 99, 132, 0.55)",
                "rgba(255, 99, 132, 0.8)",
                "rgba(255, 99, 132, 1)",
              ],
              hoverOffset: 4,
            },
          ],
        },
      });
    </script>
    <!-- Summary Error Doughnut Chart -->
    <script>
      const errorDoughnutChart = document.getElementById("errorDoughnutChart");
      new Chart(errorDoughnutChart, {
        type: "doughnut",
        data: {
          labels: ["Rest Api", "Global Variables", "Bug", "Logger", "Unexpected"],
          datasets: [
            {
              label: "Type",
              data: [{{ summary.errors.rest_api }}, {{ summary.errors.global_variables }}, {{ summary.errors.bug }}, {{ summary.errors.logger }}, {{ summary.errors.unexpected }}],
              backgroundColor: [
                "rgba(255, 205, 86, 0.1)",
                "rgba(255, 205, 86, 0.3)",
                "rgba(255, 205, 86, 0.5)",
                "rgba(255, 205, 86, 0.7)",
                "rgba(255, 205, 86, 1)"
              ],
              hoverOffset: 4,
            },
          ],
        },
      });
    </script>
    <!-- Search sync tests -->
    <script>
      (function () {
        var searchTerm, panelContainerId;
        // Create a new contains that is case insensitive
        $.expr[":"].containsCaseInsensitive = function (n, i, m) {
          return (
            jQuery(n).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0
          );
        };
        $("#sync_test_search").on("change keyup paste click", function () {
          searchTerm = $(this).val();
          $("#syncTestResultAccordion > .accordion-item").each(function () {
            panelContainerId = "#" + $(this).attr("id");
            $(
              panelContainerId +
                ":not(:containsCaseInsensitive(" +
                searchTerm +
                "))"
            ).hide();
            $(
              panelContainerId + ":containsCaseInsensitive(" + searchTerm + ")"
            ).show();
          });
        });
      })();
    </script>
    <!-- Search async tests -->
    <script>
      (function () {
        var searchTerm, panelContainerId;
        // Create a new contains that is case insensitive
        $.expr[":"].containsCaseInsensitive = function (n, i, m) {
          return (
            jQuery(n).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0
          );
        };
        $("#async_test_search").on("change keyup paste click", function () {
          searchTerm = $(this).val();
          $("#asyncTestResultAccordion > .accordion-item").each(function () {
            panelContainerId = "#" + $(this).attr("id");
            $(
              panelContainerId +
                ":not(:containsCaseInsensitive(" +
                searchTerm +
                "))"
            ).hide();
            $(
              panelContainerId + ":containsCaseInsensitive(" + searchTerm + ")"
            ).show();
          });
        });
      })();
    </script>
    <!-- Open All & Close All for Accordion -->
    <script>
      $("#sync_test_open_all").on("click", function () {
        $(
          "#syncTestResultAccordion .accordion-item .accordion-collapse"
        ).collapse("show");
      });
      $("#sync_test_close_all").on("click", function () {
        $(
          "#syncTestResultAccordion .accordion-item .accordion-collapse"
        ).collapse("hide");
      });
      $("#async_test_open_all").on("click", function () {
        $(
          "#asyncTestResultAccordion .accordion-item .accordion-collapse"
        ).collapse("show");
      });
      $("#async_test_close_all").on("click", function () {
        $(
          "#asyncTestResultAccordion .accordion-item .accordion-collapse"
        ).collapse("hide");
      });
    </script>
  </body>
</html>
"""